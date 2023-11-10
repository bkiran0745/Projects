a = (10,20,30)
print(a)
print(type(a))

print(a[1]) # Here we can access the Tuple Elenments 

x = a[0]
y = a[1]

# a[1] = x+y
# print(a[1])
'''
Error In Tuple we cannot assign the value to it
TypeError: 'tuple' object does not support item assignment

'''

# a.insert(1,200) In "Tuple" the Insertion is "NOT POSSIBLE" as in 'List'
'''
We will get AttributeError: tuple' object has no attribute 'insert' 
'''


# convert tuple to list
b=list(a) # Converting the Tuple TO List
print(b)
print(type(b)) # List

d=tuple(b) # Converting the List to Tuple again
print(d)
print(type(d)) # Tuple

z=[] # Store the Divided objects for the below code

# c = [10,12,14]
for i in b:
    x = (i // 2) # We used // bcoz to convert to Floor 
    z.append(x) # To add the Divided values to a list using append 
print(z)

t = tuple(z)
print(t)

(aa,bb,cc) = t

print(aa,bb,cc)
print(type(aa))

