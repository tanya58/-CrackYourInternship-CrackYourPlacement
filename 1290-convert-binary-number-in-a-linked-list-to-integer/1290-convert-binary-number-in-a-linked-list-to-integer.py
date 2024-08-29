# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        su = 0
        while(head):
                su = su*2
                su = su+head.val
                head = head.next
        return su   
        