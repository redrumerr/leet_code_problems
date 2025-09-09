# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        middle_pointer = head
        end_pointer = head

        while end_pointer is not None and end_pointer.next is not None:
            middle_pointer = middle_pointer.next
            end_pointer = end_pointer.next.next
        return middle_pointer
        