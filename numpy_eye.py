import numpy as np

rows, cols = list(map(int, input().split(" ")))
print(np.eye(rows, cols))
