# a = {"key":"value"} - Syntax of dictionary
# Dictionary 
'''a = {"name":"Rohan", "height": "34.45", "phone":"345345324"}
print(a["name"])
print(a["height"])
print(a["phone"])
print(a["name"], a["height"], a["phone"])'''

# Dictionary Methods
a = {"name":"Rohan", "height": "34.45", "phone":"345345324"}
print(a.items())
print(a.keys())
a.update({"weight":"12kg"})
print(a)
print(a.get("name"))