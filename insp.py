import fire


class WordlistInspector:
    ''' Inspector for wordlists '''
    def statt(self, *wordlists):
        import json
        from util.statt import group_print
        words = set()
        for wordlist in wordlists:
            with open(wordlist) as wlf:
                wl_json = json.load(wlf)

            if isinstance(wl_json, dict):
                wordlist = wl_json.keys()
            elif isinstance(wl_json, list):
                wordlist = wl_json

            words = words | set(wordlist)
        group_print(words)

    def analyze(self, *wordlists):
        from util.analyze import analyze
        analyze(wordlists)

    def analyze_statt(self, *wordlists):
        from util.statt import group_print
        from util.analyze import analyze
        analyze(wordlists, group_print)


if __name__ == '__main__':
    fire.Fire(WordlistInspector)
