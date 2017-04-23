'''
Script to wash the magoosh GRE 1000 flashcards raw text into a structured JSON.
'''

import argparse
import re
import json
from collections import OrderedDict
parser = argparse.ArgumentParser(__doc__)
parser.add_argument('-i', '--input',
                    default='magoosh-gre-1000-words_oct01.txt',
                    help='Input raw text file path')
parser.add_argument('-o', '--output',
                    help='Output JSON file path')

FLAGS = parser.parse_args()

MAGOOSH_NET = 'gre.magoosh.com'
MOST_IMPORTANT = ''.join([
    'This word has other definitions but this ',
    'is the most important one for the GRE'
])


word_levels = {'Common (High-frequency) Words',
               'Basic Words',
               'Advanced Words'}

word_definer = re.compile(r'([a-z]*) \(([a-z]*)\)\: (.*)')

obj = OrderedDict()  # JSON object of the wordlist

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
                'level': word_level
            }
            examples = []
            definitions = [define]

            # sometimes the definition of the word exceeds one line. In such
            # case we need to append the following definition lines.
            define_finished = False
        else:
            if line == MOST_IMPORTANT:
                obj[word]['extra'] = MOST_IMPORTANT
                continue

            if line[0].isupper():
                # this marks the beginning of the example sentence
                # dump the definition
                define_finished = True
                obj[word]['definition'] = ''.join(definitions)

            if not define_finished:
                if definitions[-1].endswith('-'):
                    # if the line is broken at '-', do not append with the
                    # additional space (see word 'spartan')
                    sep = ''
                else:
                    sep = ' '
                definitions.append(sep + line)

            else:
                examples.append(line)
                if line.endswith('.'):
                    # this mark the end of the example sentence
                    obj[word]['example'] = ' '.join(examples)


json.dump(obj, open(FLAGS.output, 'w'), indent=4)
