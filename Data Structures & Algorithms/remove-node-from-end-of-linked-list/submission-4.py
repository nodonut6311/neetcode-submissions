# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        prev, cur = None, head

        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp

        if n == 1:
            prev = prev.next
        else:
            i = 1
            t = prev
            while i < n - 1:
                t = t.next
                i += 1

            cur = t.next
            t.next = cur.next

        cur = prev
        prev = None
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp

        return prev
