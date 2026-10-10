class Node:
    def __init__(self,val):
        self.data=val
        self.next=None

class Linkedlist:
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

    def cal_sum_of_consecutive_nodes(self):   #!two ways to solve
        temp=self.head
        result=[]
        while temp and temp.next:
            cal=temp.data + temp.next.data
            result.append(cal)
            temp=temp.next
        return result

    # def cal_sum_of_consecutive_nodes(self):
    #         temp=self.head
    #         result=LinkedList()
    #         while temp:
    #             nextnode=temp.next
    #             if nextnode is None:
    #                 break
    #             cal=temp.data + nextnode.data
    #             result.append(Node(cal))
    #             temp=temp.next
    #         return result

    def print(self):
        temp=self.head
        # while(temp.next):
        while temp:
            print(temp.data, end=" ")
            temp=temp.next
        print()

list=Linkedlist()
n1=Node(10)
n2=Node(20)
list.append(n1)
list.append(n2)
list.append(Node(30))
list.append(Node(40))
list.append(Node(50))

list.print()
result=list.cal_sum_of_consecutive_nodes()
print(result)