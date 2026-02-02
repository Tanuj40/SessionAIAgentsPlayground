# A function is a code that runs only when u call it.

# Ex: 1
def greet(): #def <function_name>():
    print("hello")
    

greet()



def say_hi(): 
    print("hi")
    
    
    
    
    
    # parameters and arguments
    
def greetings(name): # name --> parameter
    print("Hello", name)
        
        
        
greetings("Tanuj") #Tanuj --> argument
greetings("Ankit")
greetings("Rohit")
greetings("Sonia")








# multiple parameters

# calculate a price of a product whose unit price is 300rs, and quantity is 3
def calculate_price(unit_price, quantity):
    total_price = unit_price * quantity
    print("Total Price is:", total_price)
    
calculate_price(300, 3)