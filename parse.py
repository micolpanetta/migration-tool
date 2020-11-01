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

def get_row(values, name):
    return [ row for row in values if row.startswith(name) ][0]

def parse(path):
    with open(path, 'r') as file:
        content = ''.join(file.readlines())
    values = content.split("'")

    bgm_row = get_row(values, "BGM")

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

def parse_unh(unh_row):
    return unh_row.split("+")[1]

def parse_unt(unt_row):
    return unt_row.split("+")[2]

def compute_id_data(pair):
    values_b2b = remove_last_if_empty(pair[0]["values"])
    values_see = remove_last_if_empty(pair[1]["values"])
    values = zip_longest(values_b2b, values_see, fillvalue=None)
    diff = [ (b2b_val, see_val, "OK" if b2b_val == see_val else "KO") for (b2b_val, see_val) in values ]
    ko_counter = len([ b2b_see_result for b2b_see_result in diff if b2b_see_result[2] == "KO" ])
    unh_counter = parse_unh(get_row(values_b2b, "UNH"))
    unt_counter = parse_unt(get_row(values_b2b, "UNT"))

    return  {
        "bgm": pair[0]["bgm"],
        "diff": diff,
        "ko_count": ko_counter,
        "b2b_unh_counter" : unh_counter,
        "b2b_unt_counter" : unt_counter,
        "unh_unt_result" : "OK" if unh_counter == unt_counter else "KO"

    }

def get_data(path_b2b, path_see):
    b2b_dicts = [ parse(file) for file in files_in(path_b2b) ]
    see_dicts = [ parse(file) for file in files_in(path_see) ]
    pairs = [ (b2b, find_pair(b2b, see_dicts)) for b2b in b2b_dicts ]
    pairs = [ pair for pair in pairs if pair[1] is not None ]
    ids = [ compute_id_data(pair) for pair in pairs ]
    return (b2b_dicts, see_dicts, ids)

#pp(diffs[0])
