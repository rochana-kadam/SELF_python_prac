class Node:
    def __init__(self,val):
        self.data=val
        self.next=None

class Linkedlist:
    def __init__(self):
        self.head=None

    def append(self,new_node):
        if self.head==None:
            self.head=new_node
        else:
            temp=self.head
            while(temp.next):
                temp=temp.next
            temp.next=new_node

    def concatenate(self):
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next=list2.head

    def print(self):
        temp=self.head
        # while(temp.next):
        while temp:
            print(temp.data, end=" ")
            temp=temp.next
        print()

list=Linkedlist()
n1=Node(10)
n2=Node(20)
list.append(n1)
list.append(n2)
list.append(Node(30))

list.print()

list2=Linkedlist()
n1=Node(1)
n2=Node(2)
list2.append(n1)
list2.append(n2)
list2.append(Node(3))

list2.print()

list.concatenate()
list.print()