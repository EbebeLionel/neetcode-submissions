'''
[0,1,2,3]

Null <- 0 -> 1 -> 2 -> 3
  n     h    t
  t = h
  h = n
  n = t
  h = h.next

'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = None
        curr = head
        while curr:
            temp = curr.next
            curr.next = node
            node = curr
            curr = temp

        return node

         