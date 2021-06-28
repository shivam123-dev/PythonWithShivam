## Basic Operations

##import math
##print("Hello World")
##print(math.floor(3.65))
##print(math.cos(3.65))
##print("This will run")
##a = 1
##b=3
##c = "This is me"
##print(a+b)
##print(type(c))

## String Operations

##str1 = "this is my first python string"
##print(str1)
##
##print(str1.capitalize())
##print(str1.find("this"))
##
##print(str1.upper())
##print (str1.lower())

## List

##items = [1,2,3, "shivam"]
##print(items)
##print(type(items))
##
##items[0] =  "rohan"
##print(items)

## Tuple

##tup1 = (1,2,3)
##print(tup1)
##print(type(tup1))
##tup1[0] = 4
##print(tup1)

## Dictionary

##dict1 = {}
##print(type(dict1))
##print(dict1)
##
##dict1["virat"] = 100
####print(dict1.["virat"])
##print(dict1.get("virat"))
##print(dict1.items())
##print(dict1.keys())
##dict1.update({"Sachin": 500})
##print(dict1)

## List to set

##list1 = [1,2,3,4,5,3,1]
####print(list1)
##s1 = set(list1)
##print(s1)

## Concatenation of strings 

##a = 5
##b = 10
##c = 'Shivam'
##print(str(a) + str(b) + str(c))
##print('10 - 5 is',10-5)
##print('10 + 5 is',10+5)
##print('10 * 5 is',10*5)
##print('10 // 5 is',10//5)
##print('10 / 5 is',10/5)

## Operators

##var = input()
##var = int(var)
##print(var)
##print(type(var))
##if(var > 4):
##    print("Variable is greater")
##elif (var == 4):
##    print("Variable is same")
##else:
##    print("Variable is smaller")

## Loops

##for i in range(0,101):
##    print(i)

##i = 0
##while(i<101):
##    print(i)
##    i = i+1


## Functions

##def average(num1, num2):
##    avr = (num1 + num2) / 2
##    return avr
##print(average(3,6))

## Error Handling
##index = 3
##try:
##    print(index)
##except Exception as e:
##    print(e)

## File Handling
##f = open("1.txt", "w")
##f.write("Shivam")
##f.close()

##f =  open("1.txt", "r")
##content = f.read()
##f.close()
##print(content)
