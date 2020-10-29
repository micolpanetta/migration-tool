from os import walk
from itertools import zip_longest

def files_in(path):
    files = []
    for (dirpath, dirnames, filenames) in walk(path):
        files.extend(filenames)
        break
    return [ path + '/' + f for f in files ]

def parse_bgm(bgm_row):
    return bgm_row.split("+")[2]

def parse(path):
    with open(path, 'r') as file:
        content = ''.join(file.readlines())
    values = content.split("'")

    bgm_row = [ row for row in values if row.startswith("BGM") ][0]

    return {
        "content": content,
        "values": values,
        "bgm": parse_bgm(bgm_row)
    }

def find_pair(b2b, see_dicts):
    found = [see for see in see_dicts if see["bgm"] == b2b["bgm"]]
    if len(found) == 0:
        print("Nessuna corrispondenza trovata in SEE per BGM : " + b2b["bgm"])
        return None
    return found[0]

def remove_last_if_empty(list):
    if not list:
        return list
    #check ultimo elemento stringa vuota per split
    if not list[-1]:
        return list[:-1]

    return list

def diff(pair):
    values_b2b = remove_last_if_empty(pair[0]["values"])
    values_see = remove_last_if_empty(pair[1]["values"])
    values = zip_longest(values_b2b, values_see, fillvalue=None)
    return  {
        "bgm": pair[0]["bgm"],
        "diff": [ (b2b_val, see_val, "OK" if b2b_val == see_val else "KO") for (b2b_val, see_val) in values ]
    }

def get_diffs(path_b2b, path_see):
    b2b_dicts = [ parse(file) for file in files_in(path_b2b) ]
    see_dicts = [ parse(file) for file in files_in(path_see) ]
    pairs = [ (b2b, find_pair(b2b, see_dicts)) for b2b in b2b_dicts ]
    pairs = [ pair for pair in pairs if pair[1] is not None ]
    diffs = [ diff(pair) for pair in pairs ]
    return (b2b_dicts, see_dicts, diffs)

#pp(diffs[0])
