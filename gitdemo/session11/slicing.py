import numpy as np

a = np.array([10, 20, 30, 40, 50])

# [20, 30, 40]

print(a[1:4])



# 2d slicing

matrix = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

# [[2 3]
# [5 6]]

# first 2 rows --> 0:2
# column 1 and 2 : 1:3

#print(matrix[:2, 1:3])
print(matrix[1:3, 0:3])