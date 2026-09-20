# 206. Reverse Linked List
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        back = None
        ptr = head
        while(ptr):
            tmp = ptr.next
            ptr.next = back
            back = ptr
            ptr = tmp
        return back