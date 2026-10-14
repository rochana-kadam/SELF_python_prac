class Node:
    def __init__(self,val):
        self.data=val
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None

    def append(self,new_node):
        if self.head== None:
            self.head=new_node
        else:
            temp=self.head
            while(temp.next):
                temp=temp.next
            temp.next=new_node

    def delete(self,val):
        if self.head.data==val:
           self.head=self.head.next
        else:
            temp=self.head
            prev=None

            while(temp):
                if temp.data==val:
                    break
                else:
                    prev=temp
                    temp=temp.next

            if temp is None:
                print("valur not found")
                return
            
            prev.next=temp.next
            temp=None


    def print(self):
        temp=self.head
        while(temp):
            print(temp.data, end=" ")
            temp=temp.next
        print()

list=LinkedList()
n1=Node(10)
n2=Node(20)
list.append(n1)
list.append(n2)
list.append(Node(30))
list.append(Node(40))
list.append(Node(50))

list.print()

list.delete(30)
list.print()