#Question 2
##Write a function ‘exists’ which takes a variable symbol v and returns whether v is defined.

def exists(v): 
    return str(v) in vars() or str(v) in globals()
print(exists(v))