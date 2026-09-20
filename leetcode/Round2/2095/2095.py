# 2095. Delete the Middle Node of a Linked List
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        slow = head
        fast = head.next.next

        while(fast and fast.next):
            slow = slow.next
            fast = fast.next.next
        slow.next = slow.next.next
        return head