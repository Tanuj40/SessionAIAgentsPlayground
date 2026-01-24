# basic math in Python
# operators in python

a = 11
b = 3


sum = a + b         # addition
print(sum) 


sub = a - b         # subtraction
print(sub)

mul = a * b         # multiplication
print(mul)


div = a / b         # division
print(div)


# floor --> nearest lowest integer corrresponding to float value
# 3.3333333 --> 3
# ceil --> nearest highest integer corresponding to float value
# 3.3333333 --> 4



nearest_int_div = a // b
print(nearest_int_div)

# 11 / 3
# quotient = 3
# remainder = 2


remainder = a % b   #remainder
print(remainder)
print(type(remainder))


c = 4
d = 16
# 2 to the power 4
exponent = c ** d
print(exponent)
print(type(exponent))


price = 50
quantity = 4
total = price * quantity
print(total)
print(type(total))




total_marks = 450
subjects = 5
average = total_marks / subjects
print(average)
print(type(average))

## order of executions

# 1, parenthesis
# 2, exponent
# 3, multiplication / division
# 4, addition / subtraction



result = (2 + 3) * 4 + 6 / 2

# 5 * 4 + 6 / 2
# 20 + 3.0
# 20.0 + 3.0
# 23
print(result)