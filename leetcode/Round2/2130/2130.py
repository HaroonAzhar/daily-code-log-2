# 2130. Maximum Twin Sum of a Linked List
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        back = None
        fast = head
        slow = head
        while(fast and fast.next):
            fast = fast.next.next
            slow.next, back, slow = back, slow, slow.next
        res = 0
        while(slow):
            res = max(res, slow.val + back.val)
            slow,back = slow.next, back.next
        return res