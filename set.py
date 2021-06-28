# Set:- Removes the repeated elements
s1 = {23,22,2,2,2,22,2,4,2,}
s1.add(44) # adds only 1 element at a time
s1.update([12,12,423,234234]) # adds multiple elements at a time
print(len(s1)) # prints the length of the set s1

# use discard instead of remove 
# s1.remove(1) -> strict
# s1.discard(1)
# More functions
# Like list we can use.pop, .clear, del and
# intersection, union 
print(s1)