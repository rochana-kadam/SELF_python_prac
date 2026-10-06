class Node:
    def __init__(self,val):
        self.data=val
        self.next=None

class LinkedList:
    
    def __init__(self):
        self.head=None

    def append(self,new_node):
        # cnt=0
        if self.head==None:
            self.head=new_node
        else:
            temp=self.head
            while(temp.next):
                temp=temp.next
            temp.next=new_node
            # cnt+=1
    def print(self):
        temp=self.head
        cnt=0
        while temp:
            cnt+=1
            temp=temp.next
        print(cnt)


list=LinkedList()
n1=Node(1)
list.append(n1)
list.append(Node(2))
list.append(Node(3))
list.append(Node(4))

list.print()