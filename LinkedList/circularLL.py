#!/usr/bin/env python3

class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None
       
'''CSLL1 = Node(10) # C Cricular S single LL Linked List
print(CSLL1.data)'''

class CircularSLL:
    def __init__ (self):
        self.head = None #Empty LL

    def travers_csll (self):
        if self.head is None:
            print("It is an empty LL")
            return
        n = self.head
        while True:
            print(n.data, "--->", end=" ")
            n = n.ref
            if n == self.head:
                 break
            

    def insert_begin(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            new_node.ref = self.head  # Pointing to itself to make it circular
        else:
            temp = self.head
            while temp.ref != self.head:
                temp = temp.ref
            new_node.ref = self.head
            temp.ref = new_node
            self.head = new_node

CSLL = CircularSLL()
CSLL.insert_begin(10)
CSLL.insert_begin(20)
CSLL.insert_begin(30)
CSLL.travers_csll()