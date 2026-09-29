# 2130. Maximum Twin Sum of a Linked List
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        ms = -math.inf
        slow = head
        fast = head
        back = None
        while fast and fast.next:
            fast = fast.next.next
            slow.next,slow, back = back, slow.next, slow
        while slow:
            s = slow.val + back.val
            ms = max(s,ms)
            slow, back = slow.next, back.next
        return ms