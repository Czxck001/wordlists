''' Print the supplementary part of Barron 800 wordlists
    with respect to Magoosh GRE flashcards and New GRE Upgrade
'''
import json
from util.common import load_wordlist

magoosh_path = 'wordlists/magoosh-gre'
upgrade_path = 'wordlists/gre-upgrade'

old_words = set(load_wordlist(magoosh_path)) | set(load_wordlist(upgrade_path))

barron_file_path = 'wordlists/barron-800-new/barron.json'
wordbook = dict([
    (w['word'], w['definition'])
    for w in json.load(open(barron_file_path))
    if w['word'] not in old_words
])

json.dump(wordbook, open('barron.json', 'w'), indent=4)
