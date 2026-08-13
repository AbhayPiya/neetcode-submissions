# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev,curr= None, head #TC O(n) , SP O(1) #not recursive

        while curr:
            nxt = curr.next
            curr.next = prev
            prev= curr
            curr= nxt
        return prev

##Easy option but not optimal: below code

        if not head:
            return None
        newhead = head
        if head.next:
            newhead = self.reverselist(head.next)
        head.next = None

        return newhead