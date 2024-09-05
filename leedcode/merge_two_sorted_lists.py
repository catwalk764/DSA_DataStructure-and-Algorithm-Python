#!/usr/bin/env python3
class Nodelist(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergetwolist(self, list1, list2):
        #using burteforce technique /extracting lists and sorting them

        nodes = []

        while list1:
            nodes.append(list1.val)
            list1 = list1.next
        while list2:
            nodes.append(list2.val)
            list2 = list2.next

        nodes.sort()
        
        temp = Nodelist(0)
        head = temp
        for val in nodes:
            temp.next = Nodelist(val)
            head = head.next
        return temp.next
    
    
list1 =[1,3,5]
list2 =[2,4,6]
solution = Solution()
result = solution.mergetwolist(list1, list2)
print(result)