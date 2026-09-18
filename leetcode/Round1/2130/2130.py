class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        back = None
        slow = head
        fast = head
        while(fast and fast.next):
            fast = fast.next.next
            tmp = slow.next
            slow.next = back
            back = slow
            slow = tmp
        res = 0
        while(slow):
            res = max(res,back.val + slow.val)
            back, slow = back.next, slow.next
        return res