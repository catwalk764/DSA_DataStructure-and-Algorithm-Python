#!/usr/bin/env python3

class Node: # Node class
    def __init__(self, data):
        self.data = data
        self.ref = None
'''
Node1 = Node(10)
print(Node1)
'''
class LinkedList: # LinkedList Class
    def __init__(self):
        self.head = None # Empty LinkedList

        # below are the traversal function
    def check_LL(self): # function to check LL is empty to travers.
        if self.head is None:
            print("Linked List is empty")
        else:
            n = self.head # assigning self.head into variable 'n'.
            while n is not None:
                print(n.data, "--->", end=" ")
                n = n.ref

#LL1 = LinkedList()
#LL1.check_LL()

# Below function is to insert or add element at the begining of the LL.
    def add_begin(self, data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node
   
#LL1 = LinkedList()
#LL1.add_begin(10)
#LL1.check_LL()

    def add_tail(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.ref is not None:
                n = n.ref
            n.ref = new_node
    
    def add_after(self, data, x):
        n = self.head
        while n is not None: #loop to check empty LL.
            if x == n.data: # checking the target data.
                break
            n = n.ref
        if n is None:
            print("Node is not present in the LL")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node

    def add_before(self, data, x):
        n = self.head
        
        if n is None:
            print( "Empty LL")
            return
            
        while n.ref is not None: 
            if x == n.ref.data:# checking the previous node data from the current "n" node references.
                break
            n = n.ref
        if n.ref is None:
            print("Node is not present in the LL")
        elif x == self.head.data:
            print("x is head node of LL")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node

    def ins_ele_emptyLL (self, data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
            n = self.head
            print(n.data)
        else:
            print("LL is not empty")


    def delete_start(self):
        #n = self.head
        if self.head is None:
            print("LL is empty, can't perfrom deletion")
        else:
            #self.head = n.ref
            self.head = self.head.ref

    def delete_end(self):
        if self.head is None:
            print("Since the LL is empty, can't perform the deletion")
            return
        n = self.head
        while n.ref.ref is not None:
            n = n.ref
        n.ref = None
        
    def delete_value(self, x):
        if self.head is None:
            print("LL is empty to perform delete")
            return
        n = self.head

        if self.head.data == x: # spical case to check the head node
            self.head = self.head.ref
            return 
        
        while n.ref is not None:
            if x == n.ref.data:
                break
            n = n.ref
        if n.ref is None:
            print("Node you're trying delete value is not present in the LL")
        else:
            n.ref = n.ref.ref
        


        



LL1 = LinkedList()
LL1.add_begin(10)
LL1.add_begin(20)
LL1.add_begin(30)

LL1.delete_value(30)
#LL1.delete_end()
#LL1.delete_start()
'''
LL1.add_begin(10)
LL1.add_begin(15)
LL1.add_tail(20)
LL1.add_after(60,10)

LL1.add_before(100, 20)



LL1.ins_ele_emptyLL(10)
LL1.ins_ele_emptyLL(30)
'''
LL1.check_LL()