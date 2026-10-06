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

    def odd_alternate(self):
        temp = self.head

        while temp and temp.next:
            print(temp.data)
            temp = temp.next.next

        if temp:
            print(temp.data)  #* check whether the node does exist before skipping two nodes
            

list=LinkedList()
list.append(Node(1))
list.append(Node(2))
list.append(Node(3))
list.append(Node(4))
list.append(Node(5))
list.append(Node(6))
list.append(Node(7))
list.odd_alternate()