file = "File.txt"

xx = "My Name Is Pavan g123 Name pavan Sourabh Name Name 123 xyzui !@#"

# with open(file, "r") as f:
#     content = f.readlines()

import re


def count_words(_string):
    words = re.findall(pattern=r"[a-zA-Z]+", string=_string)
    # print(words)

    counts = {}
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1


    # print(f"COUNTS : {counts}")

    # Sort The Counts
    counts_sorted = sorted(counts.items(), key=lambda x: x[1])

    # print(f"COUNT SORTED : {counts_sorted}")
    print(f"COUNTS : {counts}")

    for k, v in counts.items()[:10]:
        print(f"{k} {v}")

print(count_words(xx))
