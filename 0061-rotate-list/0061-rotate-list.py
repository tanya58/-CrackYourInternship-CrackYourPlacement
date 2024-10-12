# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head: return head

        if head.next == None: return head
        new_head = head
        t = head
        c = 0
        while t:
            t = t.next
            c = c + 1

        n = int(k%c)

        while n != 0:
            new_head = self.rotate(new_head)
            n = n - 1

        return new_head

    def rotate(self,head):
        dummy = ListNode(-200,head)
        ls = head
        cur = head.next
        while cur:
            if cur.next == None:
                break
            cur = cur.next
            ls = ls.next

        ls.next = None
        cur.next = dummy.next
        dummy.next = cur
        return dummy.next

        