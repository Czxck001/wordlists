def load_wordlist(wordlist_path):
    import json
    import pathlib
    p = pathlib.Path(wordlist_path)
    if p.is_dir():
        p /= p.parts[-1] + '.json'  # gre -> gre/gre.json
    assert p.is_file()

    with p.open() as wlf:
        wl_json = json.load(wlf)

    # the wordlist can be a structed dict or a plain list
    # return the list only
    if isinstance(wl_json, dict):
        return list(wl_json.keys())
    elif isinstance(wl_json, list):
        return wl_json


def print_dictionaries(wordlist_paths, markdown_sharps=1):
    ''' Print a chapter of the report: list of its dictionaries
    '''
    print('{} Dictionaries'.format('#' * markdown_sharps))
    for wordlist_path in wordlist_paths:
        print('- ', wordlist_path)
    print()
