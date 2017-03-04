'''
Analyze the relation of different wordlists and list the words in a
hierarchical order.

Let L = [l0, l1, ..., l(n-1)] denote the wordlists. For each word W, assign a
bool vec B(W) of length n: if W in l(i), then B(W)(i) == 1, else B(W)(i) == 0
for i in range of 0 to n.

Then, print the words in groups of decreasing order: (1, 1, 1), (1, 1, 0), ...
(0, 0, 1)
'''


def analyze(wordlist_paths, printer=None):
    from collections import defaultdict

    if printer is None:
        def printer(wordgroup):
            print(' '.join(sorted(wordgroup)))

    wordsets = []
    wordbelongs = defaultdict(lambda: [])
    allwords = set()

    # load the wordlists and get all the words
    from util.common import load_wordlist
    for wordlist_path in wordlist_paths:
        wordset = set(load_wordlist(wordlist_path))
        allwords |= wordset
        wordsets.append(wordset)

    # get belonging of each word
    for wordset in wordsets:
        for word in allwords:
            if word in wordset:
                wordbelongs[word].append(1)
            else:
                wordbelongs[word].append(0)

    # group the words by its belonging
    belongwords = defaultdict(lambda: [])
    for word, belong in wordbelongs.items():
        belongwords[tuple(belong)].append(word)

    # print the words in hierarchical order
    from util.common import print_dictionaries
    print_dictionaries(wordlist_paths)

    from itertools import product
    for hierarchical in product((1, 0), repeat=len(wordsets)):
        if hierarchical in belongwords:
            print('# Order: {}'.format(hierarchical))
            printer(belongwords[hierarchical])
