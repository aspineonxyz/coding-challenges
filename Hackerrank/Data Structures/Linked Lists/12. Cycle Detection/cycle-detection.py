"""
Detect a cycle in a linked list. Note that the head pointer may be 'None' if the list is empty.

A Node is defined as:

    class Node(object):
        def __init__(self, data = None, next_node = None):
            self.data = data
            self.next = next_node
"""

"""
I took two pointers from head. Increased one pointer by 2 with every iteration and another pointer with 1. If there is loop they will somehow meet in the loop and will return 1. If any of them encounters NULL return 0
"""

def has_cycle(head):
    if head == None or head.next == None:
        return 0
    p1 = head
    p2 = p1
    while p1 != None and p2 != None:
        p1 = p1.next
        p2 = p2.next.next
        if p1 == p2:
            return 1
    return 0
