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
        print()

        print("last node: ", temp.data)
        print("last node points to head: ",temp.next==self.head)

    def insert(self,insert_node,pos):
        if pos==1:
            temp=self.head
            while temp.next!=self.head:
                temp=temp.next
            insert_node.next=self.head
            self.head=insert_node
            temp.next=insert_node

        else:
            temp=self.head
            cnt=1
            while cnt<pos-1:
                temp=temp.next
                cnt+=1
            insert_node.next=temp.next
            temp.next=insert_node

    
list=Circular_SLL()
n1=Node(10)
n2=Node(20)
list.append(n1)
list.append(n2)
list.append(Node(30))
list.append(Node(40))
list.append(Node(50))

list.print()

list.insert(Node(25),1)
list.print()