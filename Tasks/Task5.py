'''
here we write a program to comparrision of a Variables.
'''
a = 10
b = 50

print("The < comparision is :", a < b)  # The < comparision is : True
print("The > comparision is :", a > b)  # The > comparision is : False
print("The == comparision is :", a == b)  # The == comparision is : False
print("The != comparision is :", a != b)  # The == comparision is : True
print("The >= comparision is :", a >= b)  # The == comparision is : False
print("The <= comparision is :", a <= b)  # The == comparision is : True


# a = b

c = [10, 20, 30, 50]

print(a is c) # False
print(a is c[0]) # True
print(a is not c) # True
print(a is a) # True
print(a is not a) # False

print(a in c) # True
print(a not in c) # False


# Compare Type casting and Type conversion


a = 10
b = str(a)
print(b,type(b))
c = int(b)
print(c,type(c))
print(a+c)
print(a+b)