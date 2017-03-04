import fire


class WordlistInspector:
    ''' Inspector for wordlists '''
    def statt(self, *wordlists):
        from util.statt import statt
        statt(wordlists)

    def analyze(self, *wordlists):
        from util.analyze import analyze
        analyze(wordlists)

    def analyze_statt(self, *wordlists):
        from functools import partial
        from util.statt import group_print
        from util.analyze import analyze
        analyze(wordlists, partial(group_print, markdown_sharps=2))


if __name__ == '__main__':
    fire.Fire(WordlistInspector)
