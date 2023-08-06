# Write a script to load chunks of data from given list

# data_list = list(range(105))
data_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
data_list_2 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200]
print(f'DATA_LIST: {data_list}')


# Using Generator to get chunks:
def init_generator(data_list, data_list_2):
        chunk_size = 2
        chunk_start = 0
        while chunk_start < len(data_list):
            yield list(zip(data_list[chunk_start:chunk_start + chunk_size], data_list_2[chunk_start:chunk_start + chunk_size]))
            chunk_start += chunk_size


if __name__ == '__main__':
    f = init_generator(data_list, data_list_2)
    try:
        print(next(f))
        print(f)
        print('##########')
        print(next(f))
        print('##########')
        print(next(f))
        print('##########')
        print(next(f))
        print('##########')
        print(next(f))
        print('##########')
        print(next(f))
        print('##########')
        print(next(f))
        print('##########')
        print(next(f))
        print('##########')
        print(next(f))
        print('##########')
        print(next(f))
        print('##########')
        # print(next(f))
        # print('##########')
    except StopIteration:
        print('reached at the end, reduce one next call')