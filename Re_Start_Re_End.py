import re


def start_end(pattern_string, string):
    window_size = len(pattern_string)
    matches = []
    index = 0
    while index + window_size <= len(string):
        sub_string = string[index:index + window_size]
        match = re.search(pattern_string, sub_string)
        index += 1
        if match:
            match_tup = (index - 1, (index - 1) + window_size - 1)
            matches.append(match_tup)

    if len(matches) > 0:
        for each in matches:
            print(each)
    else:
        None_tup = (-1, -1)
        print(None_tup)

    return None


if __name__ == '__main__':
    string = "aaadaa"
    pattern_string = "aa"
    start_end(pattern_string, string)
