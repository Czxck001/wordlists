'''
Script to wash the magoosh GRE 1000 flashcards raw text into a structured JSON.
'''

import argparse
import re
import json
from collections import OrderedDict
parser = argparse.ArgumentParser(__doc__)
parser.add_argument('-i', '--input', help='Input raw text file path')
parser.add_argument('-o', '--output', help='Output JSON file path')

FLAGS = parser.parse_args()

obj = OrderedDict()
meaning_pattern = re.compile(
    r'^((?P<i>i\.|ii\.|iii\.|iv\.)\s*)?' +
    r'(?P<p>v\.|n\.|adj\.|adv\.)\s*' +
    r'(?P<d>.*?)\s*' +
    r'((?P<s>s\.\s*((\w+)([,\s]+|$))+)|(?P<a>a\.\s*((\w+)([,\s]+|$))+))*$'
)

idx_tr = {
    None: 1,
    'i.': 1,
    'ii.': 2,
    'iii.': 3,
    'iv.': 4,
}


def linesiter(f):
    # eliminate stuffs between pages
    for line in f:
        if len(line.split()) == 1 and line.split()[0].isdigit():
            continue
        if line in ['all rights reserved', 'for non-commercial purposes only']:
            continue
        yield line


with open(FLAGS.input) as f:
    word_index = 1
    word = None

    struct = OrderedDict()
    for line in linesiter(f):
        # if encountered a new "num word" line
        if re.findall(r'^\s*({})\s+'.format(word_index), line):
            if word is not None:
                # record the last word
                obj[word] = struct
                struct = OrderedDict()
            word = line.split()[1]
            struct['index'] = word_index
            struct['meanings'] = []
            word_index += 1
        else:
            find_results = meaning_pattern.findall(line)
            if find_results:
                find_result = meaning_pattern.finditer(line).__next__()
                syn_result = find_result.group('s')
                ant_result = find_result.group('a')
                synonyms = syn_result[2:].strip().split(', ')\
                    if syn_result else []
                antonyms = ant_result[2:].strip().split(', ')\
                    if ant_result else []
                struct['meanings'].append({
                    'index': idx_tr[find_result.group('i')],
                    'part': find_result.group('p').strip(),
                    'definition': find_result.group('d'),
                    'synonyms': synonyms,
                    'antonyms': antonyms,
                })


json.dump(obj, open(FLAGS.output, 'w'), indent=4)
