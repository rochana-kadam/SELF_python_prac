
# * find middle node and delete it

class Node:
    def __init__(self,val):
        self.data=val
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None

    def append(self,new_node):
        if self.head==None:
            self.head=new_node
        else:
            temp=self.head
            while temp.next:
                temp=temp.next
            temp.next=new_node

    def find_del_middle(self):
        temp=self.head
        nodes=[]
        while temp:
            nodes.append(temp.data)
            temp=temp.next
        mid=len(nodes)//2
        mid_node=nodes[mid]

        temp=self.head
        prev=None
        while temp:
            if temp.data==mid_node:
                break
            else:
                prev=temp
                temp=temp.next

        prev.next=temp.next
        temp=None

    def print(self):
        temp=self.head
        while temp:
            print(temp.data, end=" ")
            temp=temp.next
        print()

list = LinkedList()
list.append(Node(10))
list.append(Node(20))
list.append(Node(30))
list.append(Node(40))
list.append(Node(50))

list.print()
list.find_del_middle()
list.print()