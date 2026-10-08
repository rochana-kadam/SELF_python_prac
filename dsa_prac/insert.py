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

    def print(self):
        temp=self.head
        while(temp):
            print(temp.data, end=" ")
            temp=temp.next

    def insert(self,insert_node,pos):
        if pos==0:
            insert_node.next=self.head
            self.head=insert_node

        temp=self.head
        cnt=0
        while temp and cnt<pos-1:
            temp=temp.next
            cnt+=1

        if temp is None:
            print("Invalid position")
            return 
    
        insert_node.next=temp.next
        temp.next=insert_node

ll = LinkedList()

ll.append(Node(10))
ll.append(Node(20))
ll.append(Node(30))
ll.append(Node(40))

ll.insert(Node(25), 5)

ll.print()
