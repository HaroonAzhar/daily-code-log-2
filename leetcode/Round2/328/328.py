# 328. Odd Even Linked List
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        slow = head
        fastcp = fast = head.next
        while(fast and fast.next):
            slow.next = fast.next
            slow = slow.next
            fast.next = slow.next
            fast = fast.next
        slow.next = fastcp
        return head