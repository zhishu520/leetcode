# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        cnt = 0

        mm = head


        while head != None:

            if cnt % 2 == 1:
                mm = mm.next

            head = head.next
            cnt += 1


        return mm







