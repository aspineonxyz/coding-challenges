"""
 Delete duplicate nodes
 head could be None as well for empty list
 Node is defined as

 class Node(object):

   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method.
"""

def RemoveDuplicates(head):
    if head == None:
        return None
    p1 = head
    p2 = p1.next
    while p2 != None:
        if p1.data == p2.data:
            while p2.data == p1.data:
                p2 = p2.next
                if p2 == None:
                    break
            p1.next = p2
        p1 = p1.next
        if p1 != None:
            p2 = p1.next
    return head
