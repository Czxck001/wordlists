#!/usr/bin/env python3

''' Statistic on words of specified wordlist
'''


def word_length_level(word):
    ''' group the words in terms with their lengths
    '''
    length = len(word)
    if length <= 6:
        return 'short'  # short words: length <= 5
    elif length <= 9:
        return 'middle'  # middle words: 6 <= length <= 8
    else:
        return 'long'  # long words: length > 8


def group_print(words):
    from collections import OrderedDict
    grouped_words = OrderedDict()
    grouped_words['short'] = []
    grouped_words['middle'] = []
    grouped_words['long'] = []

    for word in words:
        grouped_words[word_length_level(word)].append(word)

    for level, sub_words in grouped_words.items():
        print('{} words, {} words in total ({:.2f}%)'.format(
            level, len(sub_words), 100 * len(sub_words) / len(words)
        ))
        print(' '.join(sorted(sub_words)))
