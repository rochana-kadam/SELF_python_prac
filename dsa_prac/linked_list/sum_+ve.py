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
            while(temp.next):
                temp=temp.next
            temp.next=new_node

    def sum_of_pos(self):
        temp=self.head
        sum=0
        while(temp):
            if(temp.data>0):
                sum+=temp.data
            temp=temp.next
        print(sum)

list=LinkedList()
list.append(Node(2))
list.append(Node(-2))
list.append(Node(9))
list.append(Node(-7))
list.sum_of_pos()