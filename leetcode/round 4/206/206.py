# 206. Reverse Linked List
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None: return head
        back = None
        ptr = head
        while ptr:
            ptr.next, ptr, back = back, ptr.next, ptr
        return back