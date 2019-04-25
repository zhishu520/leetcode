# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        if l1 is None:
            return l2
        if l2 is None:
            return l1

        if l2.val < l1.val:
            l1, l2 = l2, l1

        t = l1

        while l1 and l2:
            if l1.next is None:
                l1.next = l2
                break
            elif l1.next.val <= l2.val:
                l1 = l1.next
            else:
                l2n = l2.next
                l2.next = l1.next
                l1.next = l2
                l2 = l2n

        return t

