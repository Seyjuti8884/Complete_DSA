arr=[1-->2-->3]
def reverse_ll(head):
    prev,curr=None,head
    while curr:
        nxt=curr.next
        curr.next=prev
        prev=curr
        curr=nxt
    return prev