def add(a, b): # a = 2, b = 3
    sum = a + b # sum = 5
    return sum # return 
    
def subtract(a, b): # a = 5, b = 1
    diff = a - b # 5 - 1 = 4
    print(diff) #4
    
    
output = add(2, 3) #sum = 5
print(output)
subtract(output, 1) # substract(5, 1)

2+ 3 - 1

output = add(2, 3)
subtract(output, 1)

def check_access(is_verified): 
    if not is_verified:
        return "Access Denied"
    else:
        print("Nice")
        print("Hello")
        print("Bye")
        return "Access Granted"
    
    
access = check_access(False) # access = "Access Denied"
print(access)