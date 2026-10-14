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

    def print(self):
        temp=self.head
        # while(temp.next):
        while temp:
            print(temp.data, end=' ')
            temp=temp.next
        print()

    def del_first_last(self):
        self.head=self.head.next
        temp=self.head
        prev=None
        while temp.next:
            prev=temp
            temp=temp.next
        prev.next=None
        temp=None

list=Linkedlist()
n1=Node(10)
n2=Node(20)
list.append(n1)
list.append(n2)
list.append(Node(30))
list.append(Node(40))
list.append(Node(50))

list.print()
list.del_first_last()
list.print()