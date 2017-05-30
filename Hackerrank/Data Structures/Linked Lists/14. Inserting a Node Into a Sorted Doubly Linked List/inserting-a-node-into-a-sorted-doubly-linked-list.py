"""
 Insert a node into a sorted doubly linked list
 head could be None as well for empty list
 Node is defined as

 class Node(object):

   def __init__(self, data=None, next_node=None, prev_node = None):
       self.data = data
       self.next = next_node
       self.prev = prev_node

 return the head node of the updated list
"""

def SortedInsert(head, data):
    if head == None:
        return Node(data)
    if data < head.data:
        return Node(data, head, head.prev)
    current = head
    while current.next != None:
        if data < current.data:
            new_node = Node(data, current, current.prev)
            current.prev.next = new_node
            current.prev = new_node
            return head
        current = current.next
    if data < current.data:
        new_node = Node(data, current, current.prev)
        current.prev.next = new_node
        current.prev = new_node
    else:
        new_node = Node(data, None, current)
        current.next = new_node
    return head
