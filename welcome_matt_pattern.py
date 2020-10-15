"""

"""
M       = input('Rows')
rows    = int(M)

columns = rows*3

symbol_1 = ".|."
symbol_2 = "-"

symbol_1_counts = list(range(1, (columns-3)//3, 2))
symbol_1_counts += reversed(symbol_1_counts)
symbol_1_counts.insert(len(symbol_1_counts)//2, 1)
symbol_2_counts = list(map(lambda x: (columns-(3*x))//2, symbol_1_counts))

patterns = []

for row in range(len(symbol_1_counts)):
    counter_2_step = symbol_2_counts[row]
    counter_1_step = symbol_1_counts[row]
    if row < (rows - 1)/2:
        # string_pattern = f"{symbol_2*counter_2_step}{symbol_1*counter_1_step}{symbol_2*counter_2_step}"
        string_pattern = "{}{}{}".format(symbol_2*counter_2_step, symbol_1*counter_1_step, symbol_2*counter_2_step)
        print(string_pattern)
    elif row > (rows - 1)/2:
        # string_pattern = f"{symbol_2 * counter_2_step}{symbol_1 * counter_1_step}{symbol_2 * counter_2_step}"
        string_pattern = "{}{}{}".format(symbol_2 * counter_2_step, symbol_1 * counter_1_step,symbol_2 * counter_2_step)
        print(string_pattern)
    else:
        symbol_2_length = (columns - len('WELCOME'))//2
        print("{}{}{}".format(symbol_2 * symbol_2_length, 'WELCOME', symbol_2 * symbol_2_length))
'''
# Enter your code here. Read input from STDIN. Print output to STDOUT
N, M = input().split(" ")

columns = int(N)
rows    = int(M)

symbol_1 = ".|."
symbol_2 = "-"

symbol_1_counts = list(range(1, (columns-3)//3, 2))
symbol_1_counts += reversed(symbol_1_counts)
symbol_1_counts.insert(len(symbol_1_counts)//2, 1)
symbol_2_counts = list(map(lambda x: (columns-(3*x))//2, symbol_1_counts))


for row in range(len(symbol_1_counts)):
    counter_2_step = symbol_2_counts[row]
    counter_1_step = symbol_1_counts[row]
    if row < (rows - 1)/2:
        string_pattern = "{}{}{}".format(symbol_2*counter_2_step, symbol_1*counter_1_step, symbol_2*counter_2_step)
        print(string_pattern)
    elif row > (rows - 1)/2:
        string_pattern = "{}{}{}".format(symbol_2*counter_2_step, symbol_1*counter_1_step, symbol_2*counter_2_step)
        print(string_pattern)
    else:
        print("{}{}{}".format(symbol_2 * (columns - len('welcomewelcome')),'welcome',symbol_2 * (columns - len('welcomewelcome'))))

'''