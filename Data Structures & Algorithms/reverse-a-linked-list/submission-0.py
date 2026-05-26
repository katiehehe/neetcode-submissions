# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        back = ListNode(head.val)
        head = head.next
        while head:
            new_node = ListNode(head.val)
            new_node.next = back
            back = new_node
            head = head.next
        return back