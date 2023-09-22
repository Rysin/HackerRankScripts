# string = "India is my country"
# #output = Aidni si ym yrtnuoc
#
# words = string.split()
# print(words)
#
# new_string = []
#
# for word in words:
#     #Changing the Case
#     if word.islower():
#         print(f'Lower _word: {word}')
#         _word = list(word)[::-1]
#         _word = "".join(_word)
#         print(_word)
#         _word.lower()
#     elif word.isupper():
#         print(f'Lower _word: {word}')
#         _word = list(word)[::-1]
#         _word = "".join(_word)
#         print(_word)
#         _word.upper()
#     elif word.istitle():
#         print(f'Title _word: {word}')
#         _word = list(word)[::-1]
#         _word = "".join(_word)
#         print(_word)
#         _word.title()
#     else:
#         print("False Case")
#
#     new_string.append(_word)
#
# text = ' '.join(new_string)
# print(text)

nums = [1, 2, 3, 7, 7, 8, 9, 10, 2, 4, 3 , 7]
nums.sort()
print(nums)
uni_nums = []
for num in nums:
    if num not in uni_nums:
        uni_nums.append(num)
print(uni_nums)