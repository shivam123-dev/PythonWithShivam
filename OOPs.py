class Employee:
    def __init__(self,gname,gsalary): # constructor with argument name
        self.name = gname
        self.salary = gsalary

shivam = Employee("Shivam",34)
print(shivam.name, shivam.salary)