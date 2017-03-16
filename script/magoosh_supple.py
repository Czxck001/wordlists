''' Print the supplementary part of New GRE Upgrade book, Barrons,
    with respect to Magoosh GRE flashcards
'''
from util.common import load_wordlist
from util.statt import group_print

magoosh_path = 'wordlists/magoosh-gre'
barron_path = 'wordlists/barron-800'
upgrade_path = 'wordlists/gre-upgrade'


magoosh_words = set(load_wordlist(magoosh_path))

barron_words = set(load_wordlist(barron_path)) - magoosh_words

upgrade_words = sorted([
    (k, v) for k, v in load_wordlist(upgrade_path, detailed=True).items()
    if k not in magoosh_words
])

# new gre upgrade
print('# New GRE Vocabulary Upgrade')
for word, struct in upgrade_words:
    print('### {}'.format(word))
    for k, meaning in enumerate(struct['meanings']):
        print('{}.  {} {}'.format(
            'i' * (k + 1), meaning['part'],  meaning['definition']
        ))
        print()
        if meaning['synonyms']:
            print('&ensp;' * 2 + 's. *{}*'.format(
                ', '.join(meaning['synonyms'])
            ))
            print()
        if meaning['antonyms']:
            print('&ensp;' * 2 + 'a. *{}*'.format(
                ', '.join(meaning['antonyms'])
            ))
            print()
    print()


# Barron's

print('# Barron\'s 800 words')
group_print(barron_words, markdown_sharps=2)
