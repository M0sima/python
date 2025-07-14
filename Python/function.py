
# Funtions
'''
def greet(name):
    return(f"Hello,{name}!")

message = greet("Bob")
print(message)

def add(a, b):
    return a + b

result = add(3, 4)
print(result)
'''

def factorial(n):
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)
    
def greet(name, greeting="Hello"):
    print(f"{greeting},{name}")

greet("Bob", "Good Morning")

