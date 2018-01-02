from util.common import load_wordlist
import json

data = json.load(open('critical_nw2.json'))['rows']
magoosh = load_wordlist('wordlists/magoosh-gre', detailed=True)
upgrade = load_wordlist('wordlists/gre-upgrade', detailed=True)

added = set(upgrade) - set(magoosh)

nnword = set()
print(len(list(added)))

for idx, datetime, word, known in data:
    if not known:
        nnword.add(word)

print(len(nnword))

json.dump(list(nnword), open('upgrade_un.json', 'w',),
          indent=4, ensure_ascii=False)
