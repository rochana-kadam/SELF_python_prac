# Q. 1 E-Commerce Product Search System
# An e-commerce company maintains product IDs in a BST to enable efficient
# product searching.
# Tasks:
# 1. Create a BST using product IDs.
# Insert the following product IDs:
# 150, 100, 200, 75, 125, 175, 250, 60, 90, 110.
# 2. Display product IDs in ascending order.
# 3. Search for product ID 175 exists.
# 4. Delete product ID 100.
# 5. Display the BST using inorder, preorder, and postorder traversals.
# 6. Find the minimum and maximum product IDs.

class Node:
    def __init__(self,val):
        self.data=val
        self.left=None
        self.right=None
class BST:
    def __init__(self):
        self.root=None
    def insert(self,newnode):
        if self.root is None:
            self.root=newnode
        else:
            temp=self.root
            while True:
                if newnode.data<temp.data:
                    if temp.left is None:
                        temp.left=newnode
                        return

                    else:
                        temp=temp.left
                else:
                    if temp.right is None:
                        temp.right=newnode
                        return
                    else:
                        temp=temp.right
    def inorder(self,root):
        if root is None:
            return
        else:
            self.inorder(root.left)
            print(root.data, end=" ")
            self.inorder(root.right)
    def search(self,key):
        temp=self.root
        while temp:
            if temp.data==key:
                return True
            elif key<temp.data:
                temp=temp.left
            else:
                temp=temp.right
                return False
    def delete(self,root,val):
        if root is None:
            return
        elif val<root.data:
            root.left=self.delete(root.left,val)
        elif val>root.data:
            root.right=self.delete(root.right,val)
        else:
            if root.left is None:
                return root.right
            if root.right is None:
                return root.left
            
            succ=self.get_successor(root)
            root.data=succ.data
            root.right=self.delete(root.right, succ.data)
        return root
    
    def get_successor(self,temp):
        temp=temp.right
        while temp.left is not None:
            temp=temp.left
        return temp

    def preorder(self,root):
        if root is None:
            return
        else:
            print(root.data,end=" ")
            self.preorder(root.left)
            self.preorder(root.right)
    def postorder(self,root):
        if root is None:
            return
        else:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.data,end=" ")
    def findminmax(self):
        temp=self.root
        while temp.left:
            temp=temp.left
        print("\nmin: ",temp.data)
        temp=self.root
        while temp.right:
            temp=temp.right
        print("\nmax: ",temp.data)


b1=BST()
b1.insert(Node(150))
b1.insert(Node(100))
b1.insert(Node(200))

b1.insert(Node(75))
b1.insert(Node(125))
b1.insert(Node(175))
b1.insert(Node(250))
b1.insert(Node(60))
b1.insert(Node(90))
b1.insert(Node(110))
b1.inorder(b1.root)
# if b1.search(175):
# print("Product id found")
# else:
# print("Product id not found")
# b1.delete(b1.root,100)
# print("\nafter deletion: ",end=" ")
# b1.inorder(b1.root)
# print("\npreorder: ",end=" ")
# b1.preorder(b1.root)
# print("\npostorder: ",end=" ")
# b1.postorder(b1.root)
b1.findminmax()