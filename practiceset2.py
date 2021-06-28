# Write a Python program to add two numbers.
'''a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
def add(a,b):
    return a+b
print("The sum of",a,"and",b,"is",add(a,b))'''

# Write a Python program to find the remainder when a number is divided by Z(Integer)
'''a = int(input("Enter dividend: "))
z = int(input("Enter divisor: "))
print("The remainder is", a%z)'''

# Check the type of the variable assigned using the input() function.
'''a = input("Enter anything: ")
a = int(a)
print(type(a))'''

# Use a comparison operator to find out whether a given variable a is greater than b or not. (Take a=34 and b=80)
'''a = 34
b = 80
if a>b:
    print(a,"is greater")
else:
    print(b,"is greater")'''

# Write a Python program to find the average of two numbers entered by the user
'''a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("The average is:", (a+b)/2) # it prints with floating point
print("The average is:", (a+b)//2) # it prints without floating point'''

# Write a Python program to calculate the square of a number entered by the user.
a = int(input("Enter a number: "))
print("The square of",a,"is",a**2)