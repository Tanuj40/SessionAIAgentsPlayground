import numpy as np

a = np.array([10,20,30])
print(a.shape)

# meaning
# 3 numbers in 1 straight line

# Real Life example:
# 3 exam score
# 3 temperature
# 3 prices

# 20 Array (Matrix)


b = np.array([
    [1, 2, 3],
    [4, 5, 6]
])
print(b.shape)











c =  np.zeros([10, 28, 28])
print(c.shape)
#print(c)
# meaning
# 10 item
# each values has 28 rows
# each row has 28 colums 


# what does np.zeros()
# created an array
# with shape (2, 3)
# Fill it with 0


# Why use it?
# when we want to creat empty dats

# 5 students, 3 subjects
print(np.zeros((5,3)))



# what does np.ones() mean?
print(np.ones((5, 3)))



# what is a shape?
# shape tells:
# how many rows
# how many columns
# how many layers


# arr-name[row][col]
z[0][1] = 12
print(z)