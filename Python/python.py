#Numeric Data

num1 = 3

print(type(num1))

num2 = 5.13

print(type(num2))

#Variables

my_variable = 9
total_count = 1
user = 'Betty'

#Invalid
second_variable = 9
user_name = 19

#Operators

#Addition(+)
#Subraction(-)
#Multiplication(*)
#Division(/)
#Exponentiation(**)
#Modulus(%)


x = 25
y = 5

print(x + y)
print(x * y)
print(x / y)
print(x - y)
print(x % y)
print(x ** y)

x = 25
x -= 5

print(x)

#Operator with strings

str1 = "Halo"
str2 = "World"

print(str1 + " " + str2)
print(str1 * 3)

#Control Statements

x = 0
if x > 0:
    print("positive")
elif x == 0:
    print("zero")
else:
    print("negative")


print('\n'.join([''.join([('❤️' if ((x*0.05)**2+(y*0.1)**2-1)**3-(x*0.05)**2*(y*0.1)**3 <= 0 else '  ') for x in range(-30, 30)]) for y in range(15, -15, -1)]))


#Loops
   
fruits = ["mango", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

numbers = [9,7,5,4,3,2]
for number in numbers:
    print(number)

#While Loops

i = 1
while i < 6:
    print(i)
    i += 1
    if i == 3:
        break # Exits the loop when the i is reached - 3

#Loop Control Statements

fruits = ["mango", "banana", "cherry", "date"]
for fruit in fruits:
    if fruit == "cherry":
         break # Exits the loop if cherry is found
    print(fruit)

print()   

for fruit in fruits:
    if fruit == "cherry":
       continue # Skips cherry and moves to the iteration
    print(fruit)
  
print()


for fruit in fruits:
    if fruit == "cherry":
      pass # Placeholder, no action is needed for cherry 
    print(fruit)






