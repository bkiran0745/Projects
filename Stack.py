# # Stack : It is a Linear DS in which we can store elements in sequential manner i.e cllection of objects
# # LIFO (Last In First Out)
# # stack in python
# class Stack:
#     def __init__(self):
#         self.items = []
#     def push(self):  # add element at the top
#         if len(self.items)>5:
#             print("Stack Overflow")
#         else:
#             data = int(input("Enter the element to push"))
#             return self.items.append(data)
#     def pop(self):   # remove element from top
#         try:
#             return self.items.pop()
#         except IndexError:
#             return "Stack Underflow"
#     def peek(self):   # get the top element without removing it
#         return self.items[-1]
#     def size(self):     # returns number of elements present in stack
#         return len(self.items)
#     def is_empty(self):      # check whether stack is empty or not
#         return len(self.items) == 0
#     def display(self):       # prints all the elements present in stack
#         for item in self.items:
#             print(item)
                    
# stack = Stack()
# stack.push()
# stack.display()
# stack.size()
# stack.is_empty()

# top = -1
class StackDemo:
    def __init__(self):
        self.items = []
    def push(self):  # add element at the top
        if len(self.items)==5:
            print("Stack Overflow")
        else:
            data = int(input("Enter the element to push :"))
            return self.items.append(data)
    def pop(self):
            try:
                return self.items.pop()
            except IndexError:
                return "Stack Underflow"
    def display(self):
        for i in self.items:
            print(i)

st = StackDemo()
while True:
    print("1.push \n2.Pop \n3.Display \n4 Exit")
    choice = input("Enter your choice ")
    if choice=='1':
        st.push()
    elif choice=="2":
        st.pop()
    elif choice=='3':
        st.display()
    elif choice=='4':
        break




# class Stack():
#     def __init__(self):
#         self.data= []
#     def push(self,data):
#         self.data.append(data)
#         print("Element pushed is :",data)
#     def pop(self):
#         x = self.data.pop()
#         print("Element poped is :",x)
#     def display(self):
#         print(self.data)

# st = Stack()
# st.push(1)
# st.push(2)
# st.push(3)
# st.push(4)
# st.display()
# st.pop()
# st.pop()

# print("The final stack is: ")
# st.display()
