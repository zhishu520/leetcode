# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        t = head.next
        p = head

        while t:

            if t.val == p.val:
                p.next = t.next
            else:
                p = t

            t = t.next

        return head
