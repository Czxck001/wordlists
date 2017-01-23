'''
Script to wash the magoosh GRE 1000 flashcards raw text into a structured JSON.
'''

import argparse
import re
import json
parser = argparse.ArgumentParser(__doc__)
parser.add_argument('-i', '--input',
                    help='Input raw text file path')
parser.add_argument('-o', '--output',
                    help='Output JSON file path')

FLAGS = parser.parse_args()

MAGOOSH_NET = 'gre.magoosh.com'
MOST_IMPORTANT = 'This word has other definitions but this is the most '
'important one for the GRE'


word_levels = {'Common (High-frequency) Words',
               'Basic Words',
               'Advanced Words'}

word_definer = re.compile(r'([a-z]*) \(([a-z]*)\)\: (.*)')

obj = {}  # JSON object of the wordlist

with open(FLAGS.input) as f:
    for line in f:
        line = line.strip()
        # ignore the meaningless lines
        if not line or line.startswith(MAGOOSH_NET) or (
            line.startswith('^L')
        ):
            continue

        if line in word_levels:
            word_level = line
            continue

        word_define_result = word_definer.findall(line)
        if word_define_result:
            word, part, define = word_define_result[0]
            obj[word] = {
                'part': part,
                'definition': define,
                'level': word_level
            }
            examples = []
        else:
            if line == MOST_IMPORTANT:
                obj[word]['extra'] = MOST_IMPORTANT
            elif not line[0].isalpha():
                obj[word]['definition'] += ' ' + line
            elif not line.endswith('.'):
                examples.append(line)
            else:
                examples.append(line)
                obj[word]['example'] = ' '.join(examples)

json.dump(obj, open(FLAGS.output, 'w'), indent=4)
