class Node:
    def __init__(self,val):
        self.data=val
        self.next=None

class Circular_SLL:
    def __init__(self):
        self.head=None

    def append(self,new_node):
        if self.head==None:
            self.head=new_node
            new_node.next=self.head

        else:
            temp=self.head
            while(temp.next!=self.head):
                temp=temp.next
            temp.next=new_node
            new_node.next=self.head

    def print(self):
        temp=self.head
        while temp.next!=self.head:
            print(temp.data, end=" ")
            temp=temp.next
        # print()

        print(temp.data)
        # print()

        print("last node: ", temp.data)
        print("last node points to head: ",temp.next==self.head)

    def delete(self,val):

        if self.head.data==val:
            temp=self.head
            while temp.next!=self.head:
                temp=temp.next
            self.head=self.head.next   #*can also write temp.next=self.head.next
            temp.next=self.head        #*               self.head=self.head.next

        else:
            temp=self.head
            prev=None
            while temp.next!=self.head:
                if temp.data==val:
                   prev.next=temp.next
                   return
                prev=temp
                temp=temp.next

            if temp.data==val:
                prev.next=temp.next

list=Circular_SLL()
n1=Node(10)
n2=Node(20)
list.append(n1)
list.append(n2)
list.append(Node(30))
list.append(Node(40))
list.append(Node(50))

list.print()

list.delete(10)
list.print()