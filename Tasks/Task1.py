'''
Here we write a program to find the id and address the variables
'''
a = 10 # Here We assign the value 10 to variable a
b = 100 # Here we assign the value 100 to variable b

# Here we print the id of the variables
print(id(a)) # 4350305784 (CHANGING)
print(id(b)) # 4350308664 (CHANGING)

# To print the memory of the variables
print(memoryview(bytes(a))) # <memory at 0x1036b9b40>
print(memoryview(bytes(b))) # <memory at 0x1036b9b40>