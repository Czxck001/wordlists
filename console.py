#!/usr/bin/env python3
''' Interactive prompt to inspect specified wordlist
'''

import json
import argparse
from collections import OrderedDict


parser = argparse.ArgumentParser(__doc__)
parser.add_argument('-l', '--list-path',
                    help='Path to wordlist JSON file')

FLAGS = parser.parse_args()

# TODO: support multiple wordlists
obj = OrderedDict(json.load(open(FLAGS.list_path)))


while True:
    print('> ', end='')
    query = input()
    if query in obj:
        for k, v in obj[query].items():
            print(k, ': ', v)
    elif query == '--':
        break
    else:
        print('"{}" not found in wordlist {}'.format(
            query, FLAGS.list_path
        ))
