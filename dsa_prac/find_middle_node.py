class Node:
    def __init__(self,val):
        self.data=val
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None

    def append(self,newnode):
        if self.head==None:
            self.head=newnode
        else:
            temp=self.head
            while(temp.next):
                temp=temp.next
            temp.next=newnode


    def find_middle_node(self):
        temp=self.head
        ll=[]
        while temp:
            ll.append(temp.data)
            temp=temp.next
        mid=len(ll)//2
        print(f"mid value is {ll[mid]}")

    def print(self):
        temp=self.head
        while(temp):
            print(temp.data, end=" ")
            temp=temp.next

list = LinkedList()

list.append(Node(10))
list.append(Node(20))
list.append(Node(30))
list.append(Node(40))
list.append(Node(50))

list.print()
list.find_middle_node()