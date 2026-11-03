# Q. 2 Write a program to perform the following operations on a Linear
# Queue
# 1. Enqueue an element into the queue
# 2. Dequeue an element from the queue
# 3. Display
# 4. Reverse the queue using stack
# 5. Merge two queues into one.
# 6. Check if two queues are identical

class Node:
    def __init__(self, val):
        self.data = val
        self.next = None

class Queue:
    def __init__(self):
        self.front=self.rear=None

    def enqueue(self, new_node):
        if self.rear:
            self.rear.next=new_node
            self.rear=new_node
        else:
            self.front=self.rear=new_node

    def dequeue(self):
        if self.front is None:
            print("Queue is empty")
            return

        temp = self.front
        print("Deleted node:", temp.data)

        self.front = self.front.next

        if self.front is None:
            self.rear = None

        temp = None

    def print(self):
        temp=self.front
        while  temp:
            print(temp.data, end=" ")
            temp=temp.next
        print()   

# Reverse the queue using stack
    def reverse(self):
        stack = []

        while self.front:
            temp = self.front
            stack.append(temp.data)
            self.dequeue()

        while stack:
            self.enqueue(Node(stack.pop()))


# Merge two queues
    def merge(self, q2):

        if q2.front is None:
            print("Second queue is empty")
            return

        if self.front is None:
            self.front = q2.front
            self.rear = q2.rear

        else:       
            self.rear.next = q2.front
            self.rear = q2.rear

        q2.front = q2.rear = None


# Check if two queues are identical
    def identical(self, q2):
        temp1 = self.front
        temp2 = q2.front

        while temp1 and temp2:
            if temp1.data != temp2.data:
                return False

            temp1 = temp1.next
            temp2 = temp2.next

        if temp1 is None and temp2 is None:
            return True

        return False

queue=Queue()
queue.enqueue(Node(1))
queue.enqueue(Node(2))
queue.enqueue(Node(3))
queue.enqueue(Node(7))
queue.enqueue(Node(4))
queue.print()

# print("reversing stack \n")
# queue.reverse()

# print("reversed stack \n")
# queue.print()

queue2=Queue()
queue2.enqueue(Node(1))
queue2.enqueue(Node(2))
queue2.enqueue(Node(3))
queue2.enqueue(Node(7))
queue2.enqueue(Node(4))
queue2.print()

# queue.merge(queue2)
# print("Merged Queue:")
# queue.print()

if queue.identical(queue2):
    print("Queues are identical")
else:
    print("Queues are not identical")