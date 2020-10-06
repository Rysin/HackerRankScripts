from collections import Counter


def merge_the_tools(string, k):
    k = int(k)
    n = len(string)
    # chunk_length = int(n / k)
    chunk_length = n//k

    chunks = []
    # Get the chunks --> n/k
    index = 0
    for _ in range(chunk_length):
        ti = string[index:index + k]
        index += k
        ori = Counter(ti)
        ori_keys = list(ori.keys())
        result = "".join(ori_keys)
        print(result)
        # print(f"\n{ti}")
    return None


if __name__ == '__main__':
    string = "AABCAAADAACA"
    k = 3
    merge_the_tools(string, k)
