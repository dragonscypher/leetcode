# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next :
            a=head.next
            t=0
            while a.val !=0:
                t+=a.val
                a=a.next
            head.next.val = t
            head.next.next = self.mergeNodes(a)
            return head.next
        return None        
