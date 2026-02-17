# from existing data

import numpy as np
np.array([1, 2, 3])


# create a numpy array with empty values os
empty_array = np.zeros(5)
print(empty_array)


# create a numpy array with value as 1 for 10 elements
one_array = np.ones(10)
print(one_array)

print(type(one_array))


# creat evenly spaces values (like range)
arange_numpy = np.arange(0, 20, 2)
print(arange_numpy)



# evenly spaced values
# linspace : lineraly spaced numbers --> it generates evenly spaced numbers between a start and end value

linear_np = np.linspace(0, 1, 5)
print(linear_np)
# means :
# start = 0
# stop = 1
# total numbers = 5
# include boath 0 and 1

# step = (stop - start) / (num