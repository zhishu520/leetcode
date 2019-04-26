# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        arr = {}
        while head:

            l = len(arr)

            if arr.has_key(head):
                return True

            arr.setdefault(head, True)
            head = head.next

        return False
