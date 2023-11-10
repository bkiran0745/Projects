# import pyttsx3
# engine = pyttsx3.init()
# engine.say("I will speak this text")
# engine.runAndWait()

# a = []
# # pirnt(a,type(a))
# b = [10,20,]
# for i in b:
#     print(len(i))
# print(b)

c = [2,10,11,17,20]
print(c)
c.insert(3,42)
print(c)
c.append(40)
print(c)
b = [100,20,29,32]
c.extend(b)
print(c)

c.sort(reverse=True)
print(c)

c.remove(20)
print(c)

# x = c[2:4]
# c.remove(x)
# print(c) Not POSSIBLE

# del c 
# print(c)


c = []

n = 5
for i in range(0,n):
    e=input('Enter element to Insert : ')
    c.append(e)
print(c)