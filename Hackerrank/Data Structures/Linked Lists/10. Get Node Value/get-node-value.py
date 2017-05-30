"""
 Get Node data of the Nth Node from the end.
 head could be None as well for empty list
 Node is defined as

 class Node(object):

   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the node data of the linked list in the below method.
"""

def GetNode(head, position):
    if head == None:
        return None
    size = 0
    current = head
    while current != None:
        size += 1
        current = current.next
    current = head
    for _ in range(size-(position+1)):
        current = current.next
    return current.data
