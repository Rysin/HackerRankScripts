#
#
# """
# [robed, cat, bored, atc, ogd, dog, lol],
# """
#
# def find_anagrames(list_):
#     anagrams = []
#
#     for i in range(len(list_)-1):
#         for j in range(1, len(list_)-1):
#             first = sorted(list_[i])
#             second = sorted(list_[j])
#             if first == second:
#                 print(f"{list_[i]} and {list_[j]} are anagrams")
#     return None


# def sort_dict(_list):
#     return _list.sort(key=lambda x: x[-1])
#     # return _list.sort(key=lambda x: x['marks'])


# def floorIt(func):
#     @floorIt
#     def divide(a, b):
#         return a / b
#
#     print(divide(77, 6))
#
#     def wrapper_function(*args, **kwargs):
#         result = func(*args, **kwargs)
#         result = int(result)
#         return result
#
#     return wrapper_function


class Student():
    std = "6"

    def __init__(self, name, roll):
        self.name = name
        self.roll = roll

    def show(self):
        print(f'name{self.name} : Roll{self.roll}')

    @staticmethod
    def isRollEven(number):
        return bool(number % 2)

    @classmethod
    def change_std(cls, number):
        print(cls.std)
        cls.std = number
        print(cls.std)

s1 = Student("Ay", 2)
s2 = Student("Rt", 3)

s1.show()
s2.show()
print(Student.isRollEven(5))
Student.change_std(55)
