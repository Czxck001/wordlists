#!/usr/bin/env python3
''' Interactive prompt to inspect specified wordlist
'''

import json
import argparse
from cmd import Cmd
import readline
from collections import OrderedDict

readline.set_completer_delims(' \t\n')


class WordlistConsole(Cmd):
    def __init__(self, worddict, dict_name=None):
        super(WordlistConsole, self).__init__()
        self._worddict = worddict
        self._dict_name = dict_name or 'dict'

    @property
    def prompt(self):
        return '({}) '.format(self._dict_name)

    def do_l(self, query):
        # TODO: remove the required 'l' command token
        if query in self._worddict:
            if isinstance(self._worddict[query], dict):
                for k, v in self._worddict[query].items():
                    print(k, ': ', v)
            elif isinstance(self._worddict[query], str):
                print(self._worddict[query])
        else:
            print('"{}" not found in wordlist {}'.format(
                query, self._dict_name
            ))

    def complete_l(self, query, line, start_index, end_index):
        return sorted([word for word in self._worddict
                       if word.startswith(query)])


if __name__ == '__main__':
    parser = argparse.ArgumentParser(__doc__)
    parser.add_argument('-l', '--list-path',
                        help='Path to wordlist JSON file')

    FLAGS = parser.parse_args()

    # TODO: support multiple wordlists
    obj = OrderedDict(json.load(open(FLAGS.list_path)))

    console = WordlistConsole(obj)
    console.cmdloop()
