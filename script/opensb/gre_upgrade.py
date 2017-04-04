''' Print the supplementary part of New GRE Upgrade book
    with respect to Magoosh GRE flashcards
'''
import json
from util.common import load_wordlist

magoosh_path = 'wordlists/magoosh-gre'
barron_path = 'wordlists/barron-800'
upgrade_path = 'wordlists/gre-upgrade'


magoosh_words = set(load_wordlist(magoosh_path))

upgrade_words = sorted([
    (k, v) for k, v in load_wordlist(upgrade_path, detailed=True).items()
    if k not in magoosh_words
])

# new gre upgrade
wordbook = {}
for word, struct in upgrade_words:
    lines = []
    for k, meaning in enumerate(struct['meanings']):
        lines.append('{}.  {} {}'.format(
            'i' * (k + 1), meaning['part'],  meaning['definition']
        ))
        lines.append('')
        if meaning['synonyms']:
            lines.append('&ensp;' * 2 + 's. *{}*'.format(
                ', '.join(meaning['synonyms'])
            ))
            lines.append('')
        if meaning['antonyms']:
            lines.append('&ensp;' * 2 + 'a. *{}*'.format(
                ', '.join(meaning['antonyms'])
            ))
            lines.append('')
    wordbook[word] = '\n'.join(lines)

json.dump(wordbook, open('gre-upgrade.json', 'w'), indent=4)
