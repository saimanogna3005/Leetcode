class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev=None
        nex=None
        cur=head
        while cur is not None:
            nex=cur.next
            cur.next=prev
            prev=cur
            cur=nex
        return prev
        