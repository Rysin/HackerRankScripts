palindromic_int, number_list = (input(), input().split(" "))

print(all((list(palindromic_int) == list(reversed(palindromic_int)), all(list(map(lambda x: int(x) > 0, number_list))))))
