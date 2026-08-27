# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        second = slow.next
        slow.next = None
        prev= None

        while second:
            next_node = second.next

            second.next = prev

            prev = second
            second = next_node
        first = head
        second = prev
        while second:

            # Save the next nodes before changing pointers.
            first_next = first.next
            second_next = second.next

            # Connect first node to second node.
            first.next = second

            # Connect second node to the next first-half node.
            second.next = first_next

            # Move to the next nodes.
            first = first_next
            second = second_next