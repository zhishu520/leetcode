# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):

    def reverseList(self, head):

        if head:
            t, _ = self.search(head)
            return t

        return None

    def search(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if head.next:
            t, r = self.search(head.next)
            r.next = ListNode(head.val)
            return t, r.next
        else:
            r = ListNode(head.val)
            return r, r
