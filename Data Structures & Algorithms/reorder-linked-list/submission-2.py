# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # deal with if there is 1 element (bc the second half of 
        # the list will be empty otherwise which is annoying 
        # to deal with)
        if head.next is None:
            return None
        # move the head pointer to 2nd half of list
        length = 0
        curr = head
        while curr is not None:
            curr = curr.next
            length += 1
        head2 = head
        print(length)
        for i in range((length - 1) // 2):
            head2 = head2.next
        temp = head2
        head2 = head2.next
        temp.next = None
        # reverse the end of the list
        curr2 = head2
        after2 = head2.next
        while after2 is not None:
            temp = after2.next
            after2.next = curr2
            curr2 = after2
            after2 = temp
        head2.next = None
        head2 = curr2
        # merge the 2 lists
        first = head
        while head is not None:
            temp = head.next
            head.next = head2
            head = head2
            head2 = temp

        


    