class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode()
        cur=dummy
        while list1!=None and list2!=None:
            if list1.val<list2.val:
                cur.next=list1
                list1=list1.next
            else:
                cur.next=list2
                list2=list2.next
            cur=cur.next
        if list1!=None:
            cur.next=list1
        if list2!=None:
            cur.next=list2
        return dummy.next