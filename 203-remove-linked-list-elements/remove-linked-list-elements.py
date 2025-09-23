# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: Optional[ListNode]
        :type val: int
        :rtype: Optional[ListNode]
        """
        if head is None:
            return head
        temp = ListNode(0)
        temp.next = head
        slow, fast = temp, head
        while fast is not None:
            if fast.val == val:
                slow.next = fast.next
            else:
                slow = fast
            fast = fast.next
        return temp.next
        