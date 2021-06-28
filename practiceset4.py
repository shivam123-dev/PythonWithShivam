#  Write a program to store seven fruits in a list entered by the user
'''a = []
i = 0
while(i < 7):
    a.append(input("Enter a fruit name: "))
    i = i+1
print(a)'''

# Write a program to accept the marks of 6 students and display them in a sorted manner
'''a = []
i = 0
while(i<6):
    a.append(float(input("Enter the total marks of student: ")))
    i = i + 1
a.sort()
print("The list is: ", end="")
print(a)'''

# Check that a tuple cannot be changed in Python
'''a = (1,2,3,4,5)
a.append() = 4
print(a)'''

# Write a program to sum a list with 4 numbers
'''a = []
i = 0
while(i<4):
    a.append(int(input("Enter a number: ")))
    i = i+1
sum = 0
j = 0
while(j < len(a)):
    sum = sum + a[j]
    j = j + 1
print(sum)'''

# Write a program to count the number of zeros in the following tuple:
# a = (7, 0, 8, 0, 0, 9)
'''a = (7, 0, 8, 0, 0, 9)
cnt = a.count(0)
print(cnt)'''

