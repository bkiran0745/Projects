a = 12
b = 12

print(type(a))
print(type(b))

# c = int(input("Enter the value"))

# print(c, type(c))


print(memoryview(bytes(a)))

a = 'hello'

print(a[0])
# a[0]='g' Immutable : can't change or modify

a = '''This is modification'''
print(a)

for i in a:
    print(i)

x = 'a' in a
y = 'z' not in a

print(x, y)
print(x+y)

