#!/usr/bin/env python3
class BST:
    def __init__ (self, key):
        self.key = key
        self.lchild = None
        self.rchild = None


#root = BST(10)

#root.lchild = BST(5)
#root.rchild = BST(15)
#print(root.key)
#print(root.lchild.key)
#print(root.rchild.key)


# reason we called sel.key is None is to valid the is it a empty tree or not. 
# If we calling insert method is possible without creating an object (root=BST()).
# If we have value in the Object root=BST(10), then if I call method of that class root.insert(20), then now tree is not empty.
# we have to call the method from the object that why we said self.key = None which meand [root = BST(None)] this is will create an empty tree.
    
    def insert(self, data): 
        if self.key is None: # Checking the Tree is empty or not
            self.key = data
            print(f"Inserted root node with key: {self.key}")
            return
        
# if the Tree is not empty, compare the root value with data to decide position left or right.
        if self.key > data:         
# if root vaue is greater than data, then we have to place the data into left side of the tree.
# here we have to check left subtree is empty or not, if empty insert the data, or else perform this insertion again recurssively.
            if self.lchild: # Condition is True if the root node has the left subtree.
                self.lchild.insert(data) # calling the insert method again to compare the value with the subtree value to find the position.
            else:
                self.lchild = BST(data) # if there is no left subtree, then create new node(Nothing but creating an Object) self.lchild Object is created with BST class.
                print(f"Inserted {data} to the left of the {self.key}")
        else:
            if self.rchild:
                self.rchild.insert(data)
            else:
                self.rchild = BST(data)
                print(f"Inserted {data} in the right of {self.key}")


    def search(self, data):
        if self.key is None:
            print("Its an Empty Tree")
            return
        if self.key == data:
            print("Search found", data) 
            return
        if self.key > data:
            if self.lchild:
                self.lchild.search(data)
            else:
                print("message from left subtree :Node is not present in the Tree")
        else:
            if self.rchild:
                self.rchild.search(data)
            else:
                print("Message from right subtree: Node is not present in the Tree")

    def preorder_travers(self):
        if self.key is None:
            print(" Tree is empty ")
            return
        print(self.key)
        if self.lchild:
            self.lchild.preorder_travers()
        if self.rchild:
            self.rchild.preorder_travers()

    def inorder_travers(self):
        if self.key is None:
            print( "Tree is empty to perform inorder operation")
            return
        if self.lchild:
            self.lchild.inorder_travers()
        print(self.key)
        if self.rchild:
            self.rchild.inorder_travers()

    def postorder_travers(self):
        if self.key is None:
            print("Tree is empty to perfrom postorder operation")
            return
        if self.rchild:
            self.rchild.postorder_travers()
        if self.lchild:
            self.lchild.postorder_travers()
        print(self.key)

    def deletion(self, data):
        if self.key is None:
            print(" Tree is empty to perform the deletion operation")
            return
        if self.key > data:
            if self.lchild:
                self.lchild = self.lchild.deletion(data) # recursion operation with deletion return value, so need variable to store it.
            else:
                print("Given node is not present in tree, message from left Subtree")
        elif self.key > data:
            if self.rchild:
                self.rchid = self.rchild.deletion(data)
            else:
                print("Given node is not present in tree, message from right Subtree")
        else:
            if self.lchild is None:
                temp = self.rchild
                self = None
                return temp
            if self.rchild is None:
                temp = self.lchild
                self = None
                return temp
            node = self.rchild
            while node.lchild:
                node = node.lchild
            self.key = node.key
            self.rchild = self.rchild.deletion(node.key)
        return self




root = BST (None)
List1 = [6, 5, 4, 25, 50, 60]
for i in List1:
    root.insert(i)

#root.search(4)
print("Preorder")
root.preorder_travers()
print()
#root.inorder_travers()
#root.postorder_travers()
root.deletion(6)
print("after preorder")
root.preorder_travers()