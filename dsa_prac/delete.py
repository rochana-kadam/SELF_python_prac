class Node:
    def __init__(self,val):
        self.data=val
        self.next=None

class LinkedList:
    def __init__(self):
        self.head==None

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
            print(temp.data)
            temp=temp.next
