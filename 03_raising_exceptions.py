def increment(num):
    try:
        return int(num) + 1
    except:
        raise ValueError('This is not good - Shivam')
    
a = increment('364dd')
print(a)