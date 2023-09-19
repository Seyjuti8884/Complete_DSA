#arr=[1,1,2,2,3,3,4]
def remove_dupliactes(head):
    curr=head
    while curr.next!=None:
        if curr.data==curr.next.data:
            curr.next=curr.next.next
        else:
            curr=curr.next
    return head