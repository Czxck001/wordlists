''' Print the supplementary part of Barron 800 wordlists
    with respect to Magoosh GRE flashcards and New GRE Upgrade
'''
import json
from util.common import load_wordlist

magoosh_path = 'wordlists/magoosh-gre'
upgrade_path = 'wordlists/gre-upgrade'

old_words = set(load_wordlist(magoosh_path)) | set(load_wordlist(upgrade_path))

barron_file_path = 'wordlists/barron-800-new/barron.json'
barron_words = sorted([
    (w['word'], w['definition'])
    for w in json.load(open(barron_file_path))
    if w['word'] not in old_words
])

print('# Barron Supplementary ({} words)'.format(len(barron_words)))
for word, defi in barron_words:
    print('### {}'.format(word))
    print(defi)
    print()
