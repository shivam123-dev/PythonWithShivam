# name = "Shivam"
# print(name)
# name1 = ''' Shivam 

#         is a good boy'''
# print(name1)

# Slicing i=of strings
# print(name[0]) # prints first character
# print(name[2])
# print(name[2:4]) # prints from 2nd to 3rd character
# print(name[2:5]) 

# Striping of strings
# name = "    Shivam         "
# print(name)
# print(name.strip()) # removes the extra spaces

# Length of strings
# name = "Shivam"
# print(len(name)) #prints the length of the string

# More functions for manipulating strings in python
# name = "Shivam"
# name1 = "Shivam, Rohan, Shubham, Vikrant"
# var1 = name.lower() # prints the string in lowercase
# print(var1)
# var2 = name.upper() # prints the string in uppercase
# print(var2)
# var3 = name.replace("h","t") # replaces the h with t
# print(var3)
# var4 = name1.replace(", ","\n")
# print(var4)


# stri = "This is a "
# name = "shivam"
# stri2 = "This is not a"
# print(stri + name) # concatenates the string

# Making templates
name1 = "Shivam"
name2 = "Rohan"

temp = "This is a {0} and he is a good boy named {1}".format(name1,name2)

temp = "This is a {1} and he is a good boy named {0}".format(name1,name2)

temp = f'This is a {name1} and he is a good boy {name2}'

print(temp)