# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        temp1 = headA
        temp2 = headB
        hashmap = set()
        while temp1 is not None:
            hashmap.add(temp1)
            temp1 = temp1.next
        
        while temp2 is not None:
            if temp2 in hashmap:
                return temp2
            temp2 = temp2.next
        