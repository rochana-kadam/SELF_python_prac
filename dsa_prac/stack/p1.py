# Create a Stack with following operations
# 1. Push
# 2. Pop
# 3. Display

# 5. Reverse Stack using another Stack

class Node:
    def __init__(self,val):
        self.data=val
        self.next=None

class LinkedList:
    def __init__(self):
        self.top=None

    def isempty(self):
        return self.top is None

    def push(self,new_node):
        new_node.next=self.top
        self.top=new_node

    def pop(self):
        if self.isempty():
            print("stack is empty")
        else:
            temp=self.top
            print(temp.data, end=" ")
            self.top=self.top.next
            temp=None

    def print(self):
        if self.isempty():
            print("stack is empty")
        else:
            temp=self.top
            while temp:
                print(temp.data, end=" ")
                temp=temp.next
            print()

    def reverse(self):
        temp=self.top
        while temp:
            stack2.push(Node(temp.data))
            temp=temp.next


my_stack=LinkedList()
# stack2=LinkedList()
# my_stack.push(Node(10))
# my_stack.push(Node(20))
# my_stack.push(Node(30))
# my_stack.push(Node(40))
# my_stack.push(Node(50))
# my_stack.print()
# my_stack.reverse()
# stack2.print()

str = input("Enter string: ")
for i in range(len(str)):
    my_stack.push(Node(str[i]))

while not my_stack.isempty():
    my_stack.pop()