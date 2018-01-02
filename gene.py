import json

magoosh = json.load(open('magoosh.json'))
upgrade = json.load(open('gre-upgrade.json'))

un_words = set(json.load(open('un.json')))

bigdict = dict(magoosh, **upgrade)
crtdict = {k: v for k, v in bigdict.items() if k in un_words}

print(len(crtdict))

json.dump(bigdict, open('big.json', 'w'), indent=4, ensure_ascii=False)
json.dump(crtdict, open('critical2.json', 'w'), indent=4, ensure_ascii=False)
