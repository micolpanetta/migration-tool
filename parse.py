from os import walk
from itertools import zip_longest


def parse_files(path_b2b, path_see, segment):
    b2b = [parse(file, segment) for file in files_in(path_b2b)]
    see = [parse(file, segment) for file in files_in(path_see)]
    b2b = [x for x in b2b if x is not None]
    see = [x for x in see if x is not None]
    pairs = make_pairs(b2b, see, segment)
    ids = [compute_id_data(pair) for pair in pairs]
    return b2b, see, ids


def parse(file_path, segment):
    with open(file_path, 'r') as file:
        content = ''.join(file.readlines())
    values = remove_last_if_empty(content.split("'"))
    segment_row = get_row_by_key(values, segment)
    if not segment_row:
        print("Il file " + file_path + " non contiene il segmento " + segment + ". Il file non verrà considerato.")
        return None
    return {
        "content": content,
        "values": values,
        "segment": parse_segment(segment_row)
    }


def files_in(path):
    files = []
    for (dirpath, dirnames, filenames) in walk(path):
        files.extend(filenames)
        break
    return [path + '/' + f for f in files]


def make_pairs(b2b, see, segment):
    pairs = [(b2b, find_pair(b2b, see, segment)) for b2b in b2b]
    pairs = [pair for pair in pairs if pair[1] is not None]
    return pairs


def parse_segment(segment_row):
    return segment_row.split("+")[2]


def get_row_by_key(values, name):
    matches = [row for row in values if row.startswith(name)]
    if not matches:
        return None
    return matches[0]


def find_pair(b2b, see_dicts, segment):
    found = [see for see in see_dicts if see["segment"] == b2b["segment"]]
    if len(found) == 0:
        print("Nessuna corrispondenza trovata in SEE per " + segment + ": " + b2b["segment"])
        return None
    return found[0]


def remove_last_if_empty(list):
    if not list:
        return list
    # check ultimo elemento stringa vuota per split
    if not list[-1]:
        return list[:-1]

    return list


def parse_unh(unh_row):
    return unh_row.split("+")[1]


def parse_unt(unt_row):
    return unt_row.split("+")[2]


def compute_id_data(pair):
    values_b2b = pair[0]["values"]
    values_see = pair[1]["values"]
    values = zip_longest(values_b2b, values_see, fillvalue=None)
    unh_counter = parse_unh(get_row_by_key(values_b2b, "UNH"))
    unt_counter = parse_unt(get_row_by_key(values_b2b, "UNT"))
    diff = [(b2b_val, see_val, result_check(b2b_val, see_val)) for (b2b_val, see_val) in values]

    return {
        "segment": pair[0]["segment"],
        "diff": diff,
        "ko_count": len([b2b_see_result for b2b_see_result in diff if b2b_see_result[2] == "KO"]),
        "b2b_unh_counter": unh_counter,
        "b2b_unt_counter": unt_counter,
        "unh_unt_result": result_check(unh_counter, unt_counter)
    }


def result_check(first_value, second_value):
    return "OK" if first_value == second_value else "KO"
