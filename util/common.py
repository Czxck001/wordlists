def load_wordlist(wordlist_path, detailed=False):
    ''' Load a wordlist from single file, or a folder.
        If detailed, the wordlist must be structed, i.e. a dict, and the
        function will return a structured dict.
    '''
    import json
    from pathlib import Path
    root = Path(wordlist_path)
    if root.is_dir():
        json_paths = [path for path in root.iterdir()
                      if path.is_file() and path.suffix == '.json']
    elif root.is_file():
        json_paths = [root]
    else:
        raise RuntimeError('Wordlist path {} is invalid.'.format(
            wordlist_path
        ))

    if detailed:
        # the wordlist must be a dict, with keys as words, values as
        # respective structured informations
        wordlist = {}
        for json_path in json_paths:
            wl_json = json.load(json_path.open())
            assert isinstance(wl_json, dict)
            wordlist.update(wl_json)
    else:
        # the wordlist can be a structed dict or a plain list
        # return the list only
        wordlist = []
        for json_path in json_paths:
            wl_json = json.load(json_path.open())
            if isinstance(wl_json, dict):
                wordlist.extend(list(wl_json.keys()))
            elif isinstance(wl_json, list):
                wordlist.extend(wl_json)
    return wordlist


def print_dictionaries(wordlist_paths, markdown_sharps=1):
    ''' Print a chapter of the report: list of its dictionaries
    '''
    print('{} Dictionaries'.format('#' * markdown_sharps))
    for wordlist_path in wordlist_paths:
        print('- ', wordlist_path)
    print()
