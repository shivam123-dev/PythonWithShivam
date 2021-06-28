# Write a program to create a dictionary of Hindi words with values as their English translation. Provide the user with an option to look it up!

d = {}
i = 0
while (i<3):
    key = input("Enter a key: ")
    value = input("Enter a value")
    d[key] = value; # used for inserting the key with value in dictionary
    i = i+1
print(d)