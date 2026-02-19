import numpy as np

# generate 5 numbers between 0 and 1
print(np.random.rand(5))


# most numbers will be around 0 both +ve and 0ve and some might  far from 0
print(np.random.randn(5))






# random integers
print(np.random.randint(0, 20, (5, 5)))




# Seeds
print(np.random.seed(42))