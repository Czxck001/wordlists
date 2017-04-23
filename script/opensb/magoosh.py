''' Print the supplementary part of New GRE Upgrade book
    with respect to Magoosh GRE flashcards
'''
import json
from util.common import load_wordlist

magoosh_path = 'wordlists/magoosh-gre'

magoosh_words = load_wordlist(magoosh_path, detailed=True)

# new gre upgrade
wordbook = {}
for word, struct in magoosh_words.items():
    lines = [
        '**{}**: {}'.format(struct['part'], struct['definition']),
        '',
        '> {}'.format(struct['example']) if 'example' in struct else '',
        '',
        struct['extra'] if 'extra' in struct else ''
    ]
    wordbook[word] = '\n'.join(lines)

json.dump(wordbook, open('magoosh.json', 'w'), indent=4)
