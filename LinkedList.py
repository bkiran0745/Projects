# Linked List is stored in a continuous memory location by node.
import time
class Node():
    def __init__(self,data):
        self.data = data
        self.next = None

# To initailize the head as a starting part of the linked list
class initialHead():
    def __init__(self):
        self.head = None

    def insert(self):
        e = input()
        self.data = e
        self.next = None
    
    def display(self):
        pv = self.head
        while pv:
            print(pv.data)
            # time.sleep(0.3)
            pv = pv.next

e1 = initialHead()
e1.head = Node(10)
e2 = Node(20)
e3 = Node(40)
e1.head.next = e2
e2.next = e3

# To Make it as a circular linked list
# e3.next = e1.head 

e3.next = None
# while e3.next == None:
# print(e1.head.data)
# print(e1.head.next)
# print(e2.data)
# print(e2.next)
# print(e3.data)
# print(e3.next)
e1.display()
e1.insert(100)