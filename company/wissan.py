list_1 = [95, 39, 5, 78, 11, 63, 95, 11, 3, 88, 105]


for i in range(len(list_1) - 1):
    swap = False
    for j in range(len(list_1) - 1):
        swap = False
        print(list_1[j])
        print(list_1[j + 1])
        if list_1[j] > list_1[j + 1]:
            list_1[j], list_1[j + 1] = list_1[j + 1], list_1[j]
            swap = True

        print(j)


print(list_1)
print(list_1[-3])

list_2 = []
for i in list_1:
    if i not in list_2:
        list_2.append(i)

print(list_2)
print(list_2[-3])
