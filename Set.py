c = {12,10,2,10,100,100,12}
print(c)
print(type(c))

x = sorted(c)
# y = sorted(c, reverse=True)
print(x)
# print(y)

for i in c:
    print(i)

b = set((12,11,13,12,14,15,14))
print(b)
print(type(b))

a = list(b)
print(a)
print(type(a))

d = tuple(b)
print(d)
print(type(d))

p = {12,10}
print(p in c) # Here It is not possible to check a set in a set 
q = 12
print(q in c) # It is POSSIBLE to search a element in a set but not a SET


c.add(12233)
print(c)

print(b)

z = {'a','b','c','d'}
c.update(z)
print(c)

c.union(b)
print(c)
print(len(c))

d = {10,12}
e = {14,16,17,18,19,20}
x = d.union(e)
print(x)

'''
d.remove(1000)
print(d)
We will get a KeyError bcoz 1000 is not present
'''