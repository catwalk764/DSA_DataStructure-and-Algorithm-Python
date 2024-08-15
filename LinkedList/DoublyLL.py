#!/usr/bin/env python3

class Node:
    def __init__(self, data):
        self.data = data
        self.pref = None # pref --> previous link
        self.nref = None # nref --> link to the next node.

'''Node1 = Node(10)
print(Node1.data) This will create the node with data 10'''

class Doublell:
    def __init__(self):
        self.head = None
    
    def traverse_LL (self):
        if self.head is None:
            print("It is a empty LL")
        else:
            n = self.head
            while n is not None:
                print(n.data,"--->", end=" ")
                n = n.nref

    def traverse_LL_revers (self):
        if self.head is None:
            print("It is an empty LL")
        else:
            n = self.head
            while n.nref is not None:
                n = n.nref
            while n is not None:
                print(n.data, "--->", end=" ")
                n = n.pref
                


    def insert_begin(self, data):
        new_node = Node(data)
        new_node.nref = self.head
        if self.head is not None:
            self.head.pref = new_node
        self.head = new_node


    def insert_tail(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
             n = self.head
             while n.nref is not None:
                n = n.nref
             n.nref = new_node
             new_node.pref = n
    
    def insert_before(self, data, x):
        new_node = Node(data)
        if self.head is None:
            print("Empty list")
            return
        if self.head.data == x:
            new_node.nref = self.head
            self.head.pref = new_node
            self.head = new_node


        n = self.head
        while n is not None:
            if x == n.data:
                new_node.nref = n
                new_node.pref = n.pref
                return
            n = n.nref



        




DLL1 = Doublell()
DLL1.insert_begin(10)
DLL1.insert_begin(20)
DLL1.insert_begin(30)
#DLL1.insert_tail(30)
DLL1.traverse_LL_revers()
#DLL1.insert_before(100, 10)
#DLL1.traverse_LL()


