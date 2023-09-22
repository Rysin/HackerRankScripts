# Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1
#
# Input: s = "abb"
# Output: 0
#
# Input: s = "abababcda"
# Output: 6
#
# Input: s = "aabb"
# Output: -1

# Find Repeating Pattern
# Find counts chars

# s = "abababcda"
s = ""
assert len(s) != 0

letters_in_sequence = list(s)
print(letters_in_sequence)
unique_chars = list(set(letters_in_sequence))

counts = dict.fromkeys(unique_chars, 0)
print(counts.items())

for letter in letters_in_sequence:
    counts[letter] += 1
    if counts[letter] > 1:
        continue

print(counts)

# Non-Repeating Chars
non_repeat_chars = [char for char in counts if counts[char] < 2]
print(non_repeat_chars)

if non_repeat_chars:
    index = dict.fromkeys(non_repeat_chars)
    # Find Index
    for char in non_repeat_chars:
        for i in range(len(letters_in_sequence)):
            if letters_in_sequence[i] == char:
                index[char] = i
                break
    print(index)
    # Find starting index
    letter = min(index)
    print(index[letter])
else:
    print('-1')


