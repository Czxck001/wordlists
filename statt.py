#!/usr/bin/env python3

''' Statistic on words of specified wordlist
'''

import json
import argparse
from collections import OrderedDict


parser = argparse.ArgumentParser(__doc__)
parser.add_argument('-l', '--list-path',
                    help='Path to wordlist JSON file')

FLAGS = parser.parse_args()

# TODO: support multiple wordlists
obj = json.load(open(FLAGS.list_path))

if isinstance(obj, dict):
    words = list(obj.keys())
elif isinstance(obj, list):
    words = obj


def word_length_level(word):
    ''' group the words in terms with their lengths
    '''
    length = len(word)
    if length <= 5:
        return 'short'  # short words: length <= 5
    elif length <= 8:
        return 'middle'  # middle words: 6 <= length <= 8
    else:
        return 'long'  # long words: length > 8


grouped_words = OrderedDict()
grouped_words['short'] = []
grouped_words['middle'] = []
grouped_words['long'] = []


for word in words:
    grouped_words[word_length_level(word)].append(word)

for level, words in (grouped_words).items():
    print(level, 'words:')
    print(' '.join(sorted(words)))
