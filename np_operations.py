import numpy as np

rows, cols = list(map(int, input().split(' ')))

A = np.array(list(map(int, input().split(' '))))
B = np.array(list(map(int, input().split(' '))))

print(A + B)
print(A - B)
print(A * B)
print(A // B)
print(A ** B)