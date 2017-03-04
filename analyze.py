'''
Analyze the relation of different wordlists and list the words in a
hierarchical order.
'''
import json
import argparse
from collections import defaultdict

parser = argparse.ArgumentParser(__doc__)
parser.add_argument('-l', '--wordlists', nargs='+',
                    help='list of wordlist json files')
FLAGS = parser.parse_args()

wordlists = []
wordcounts = defaultdict(lambda: 0)
maxcount = 0
allwords = set()

# load the wordlists and count the frequency of each word
for wordlist_path in FLAGS.wordlists:
    with open(wordlist_path) as f:
        wl_json = json.load(f)

    if isinstance(wl_json, dict):
        wordlist = wl_json.keys()
    elif isinstance(wl_json, list):
        wordlist = wl_json

    newwords = []
    for word in wordlist:
        wordcounts[word] += 1
        if maxcount < wordcounts[word]:
            maxcount = wordcounts[word]

        # only obtain words not included in previous wordlists
        if word not in allwords:
            allwords.add(word)
            newwords.append(word)

    wordlists.append(newwords)

# group, sort and print
for k, wordlist in enumerate(wordlists):
    print('Wordlist {}'.format(k))
    countwords = defaultdict(lambda: [])
    for word in wordlist:
        countwords[wordcounts[word]].append(word)
    wordgroups = sorted(countwords.items(), key=lambda x: x[0], reverse=True)
    for lv, wordgroup_kv in enumerate(wordgroups):
        print('Level {}'.format(lv))
        print(' '.join(sorted(wordgroup_kv[1])))
