# # List Extension
# list_1 = [1, 4, 6, 86, 33]
# list_2 = ["a", "b", ["x", "y", "z"]]
# list_3 = [100, (22, 34), {7: 49, 8: 64, 9: 81}]
# tup_1 = (71, 72, (87, 89))
#
# # list_1.append(list_2)
# list_1.extend(tup_1)
# print(list_1)
# list_1 = [1, 4, 6, 86, 33]
# list_1.append(tup_1)
# print(list_1)
#
#
# # Sum of Numbers
# def sumit(n):
#     return sum(range(n + 1))
#
#
# def range_study(start, stop, interval=1):
#     _range = [i for i in range(start, stop, interval)]
#     return _range
#
#
# x = range_study(10, 30)
# print(x, sep=" ")
# x = range_study(10, 30, 3)
# print(x, sep=" ")
# x = range_study(30, 10, -3)
# print(x, sep=" ")
#
# # Dictionary Formation
# dict_1 = {2, 3, (4, 5)}
# print(dict_1)
# print(type(dict_1))

# print('A' + 'B' if '12'.isdigit() else 'X' + 'Y')
# print('12'.isdigit())

########################################################################################################################

"""100. Write a Python program to find four positive even integers whose sum is a given integer.
Input:
n = 100
Output:
[94, 2, 2, 2]
Input:
n = 1000
Output:
[994, 2, 2, 2]"""


def find_n_fragments_sum_with_even(number, n):
    frags = [2 for _ in range(n - 2)]
    frags.insert(0, number - sum(frags))
    print(frags)

    frags_avg = [sum(frags) / len(frags) for frag in frags]
    print(frags_avg)
    print(f"Sum of AVG frags is : {sum(frags_avg)}")


# find_n_fragments_sum_with_even(100, 4)
# find_n_fragments_sum_with_even(100, 6)
# find_n_fragments_sum_with_even(100, 5)
# find_n_fragments_sum_with_even(87, 5)


def find_n_fragments_sum_with_odd(number, n, base):
    frags = [base for _ in range(n - 1)]
    frags.insert(0, number - sum(frags))
    print(frags)

    frags_avg = [sum(frags) / len(frags) for frag in frags]
    print(frags_avg)
    print(f"Sum of AVG frags is : {sum(frags_avg)}")


# find_n_fragments_sum_with_odd(100, 4, 3)
# find_n_fragments_sum_with_odd(100, 6, 3)
# find_n_fragments_sum_with_odd(100, 5, 3)
# find_n_fragments_sum_with_odd(87, 5, 3)

########################################################################################################################

"""
99. Write a Python program to find a string such that, when three or more spaces are compacted to a '-' and one or 
two spaces are replaced by underscores, leads to the target. 
Input: Python-Exercises 
Output: Python Exercises 

Input: Python_Exercises 
Output: Python Exercises 

Input: -Hello,_world!__This_is-so-easy!- 
Output: Hello, world! This is so 
easy!
"""


def condition_string_on_symbols(string, symbol_list):
    _chars = list(string)
    for i in range(len(_chars)):
        if _chars[i] in symbol_list:
            _chars[i] = " "

    return "".join(_chars)


sym_list = ["-", "_"]
# print(condition_string_on_symbols("Python-Exercises", sym_list))
# print(condition_string_on_symbols("Python_Exercises", sym_list))
# print(condition_string_on_symbols("-Hello,_world!__This_is-so-easy!-", sym_list))
########################################################################################################################

"""
98. Given a string consisting of groups of matched nested parentheses separated by parentheses, write a Python program to compute the depth of each group.
Input: (()) (()) () ((()()()))
Output:
[2, 2, 1, 3]
Input: () (()) () () () ()
Output:
[1, 2, 1, 1, 1, 1]
Input: (((((((()))))))) () (()) ((()()()))
Output:
[8, 1, 2, 3]
"""


def find_depth_of_each_group(string):
    group_list = string.split()

    depth_counts = []
    for each in group_list:
        _chars = list(each)
        depth = 0
        for i in range(len(_chars) - 1):
            if _chars[i] == _chars[i + 1]:
                depth += 1
            else:
                break
        depth_counts.append(depth + 1)

    return depth_counts


#
# inputs = ["(()) (()) () ((()()()))", "() (()) () () () ()", "(((((((()))))))) () (()) ((()()()))"]
#
# for _input in inputs:
#     print(find_depth_of_each_group(_input))
########################################################################################################################

"""
97. Write a Python program to find the following strange sort of list of numbers: the first element is the smallest, the second is the largest of the remaining, the third is the smallest of the remaining, the fourth is the smallest of the remaining, etc.
Input:
[1, 3, 4, 5, 11]
Output:
[1, 11, 3, 5, 4]
Input:
[27, 3, 8, 5, 1, 31]
Output:
[1, 31, 3, 27, 5, 8]
Input:
[1, 2, 7, 3, 4, 5, 6]
Output:
[1, 7, 2, 6, 3, 5, 4]
"""


def strange_sort(_list):
    """
    algo
    1. find max of list, append it to result
    2. Find min of list, append it to result.
    3. Remove max of list, min of List
    4. Use the updated list for next interation
    """
    new_list = []
    copy_list = _list.copy()
    while len(copy_list) != 0:
        curr_max = max(copy_list)
        curr_min = min(copy_list)
        if curr_max != curr_min:
            new_list.append(curr_min)
            new_list.append(curr_max)
            copy_list.remove(curr_min)
            copy_list.remove(curr_max)
        else:
            new_list.extend(copy_list)
            copy_list = []

    return new_list


# inputs = [[1, 3, 4, 4, 4, 4, 5, 11], [27, 3, 8, 5, 1, 31], [1, 2, 7, 3, 4, 5, 6]]
# for _input in inputs:
#     print(strange_sort(_input))

########################################################################################################################


"""
92. Write a Python program to start with a list of integers, keep every other element in place and otherwise sort the list.
Input:
[2, 5, 6, 3, 1, 4, 34]
Output:
[1, 5, 2, 3, 6, 4, 34]
[1, 5, 2, 3, 6, 4, 34]
Input:
[8, 0, 7, 2, 9, 4, 1, 2, 8, 3]
Output:
[1, 0, 7, 2, 8, 4, 8, 2, 9, 3]
"""


def alternate_sort(_list):
    list_1 = []
    for i in range(0, len(_list), 2):
        list_1.append(_list[i])

    list_1.sort()

    for i in range(0, len(_list), 2):
        print(_list[i])
        _list[i] = list_1.pop(0)
        print(_list[i])

    return _list


# inputs = [[2, 5, 6, 3, 1, 4, 34], [8, 0, 7, 2, 9, 4, 1, 2, 8, 3]]
# for _input in inputs:
#     print(alternate_sort(_input))
########################################################################################################################

"""
78. Write a Python program to find the two closest distinct numbers in a given list of numbers.
Input:
[1.3, 5.24, 0.89, 21.0, 5.27, 1.3]
Output:
[5.24, 5.27]
Input:
[12.02, 20.3, 15.0, 19.0, 11.0, 14.99, 17.0, 17.0, 14.4, 16.8]
Output:
[14.99, 15.0]
"""


def closed_distinct_numbers(_list):
    sorted_list = _list.sort()

    _list = list(set(_list))
    diffs = [abs(_list[i] - _list[i + 1]) for i in range(len(_list) - 1)]
    minimum_diff_index = diffs.index(min(diffs))

    return _list[minimum_diff_index], _list[minimum_diff_index + 1]


# inputs = [[1.3, 5.24, 0.89, 21.0, 5.27, 1.3], [12.02, 20.3, 15.0, 19.0, 11.0, 14.99, 17.0, 17.0, 14.4, 16.8]]
# # for _input in inputs:
# #     print(closed_distinct_numbers(_input))
########################################################################################################################

"""
4. We are making n stone piles! The first pile has n stones. If n is even, then all piles have an even number of stones. 
If n is odd, all piles have an odd number of stones. Each pile must more stones than the previous pile but as few as 
possible. Write a Python program to find the number of stones in each pile.
Input: 2
Output:
[2, 4]
Input: 10
Output:
[10, 12, 14, 16, 18, 20, 22, 24, 26, 28]
Input: 3
Output:
[3, 5, 7]
Input: 17
Output:
[17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49]
"""


def create_stone_pile(n):
    stone_pile = list(range(n, (n + 2 * n), 2))
    return stone_pile


# inputs = [2, 3, 17]
# for _input in inputs:
#     print(create_stone_pile(_input))
########################################################################################################################

"""
10. Given a string consisting of whitespace and groups of matched parentheses, write a Python program to split it into 
groups of perfectly matched parentheses without any whitespace.
Input:
( ()) ((()()())) (()) ()
Output:
['(())', '((()()()))', '(())', '()']
Input:
() (( ( )() ( )) ) ( ())
Output:
['()', '((()()()))', '(())']
"""


def strip_white_space_and_group(string):
    ls = []
    s2 = ""
    for s in string.replace(" ", ""):
        s2 += s
        if s2.count("(") == s2.count(")"):
            ls.append(s2)
            s2 = ""
    return ls


# inputs = ["( ()) ((()()())) (()) ()", "() (( ( )() ( )) ) ( ())" ]
# for _input in inputs:
#     print(strip_white_space_and_group(_input))

########################################################################################################################

"""
12. Write a Python program to check whether the given strings are palindromes or not. Return True otherwise False.
Input:
['palindrome', 'madamimadam', '', 'foo', 'eyes']
Output:
[False, True, True, False, False]
"""


def check_palindrom(string_list):
    return [bool(list(string) == list(string)[::-1]) for string in string_list]


# inputs = ['palindrome', 'madamimadam', '', 'foo', 'eyes']
# print(check_palindrom(inputs))

########################################################################################################################
