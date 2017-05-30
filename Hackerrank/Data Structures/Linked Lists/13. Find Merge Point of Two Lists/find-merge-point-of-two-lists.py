"""
 Find the node at which both lists merge and return the data of that node.
 head could be None as well for empty list
 Node is defined as

 class Node(object):

   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node
"""

def FindMergeNode(head_a, head_b):
    nodes_a = set()
    current_a = head_a
    while current_a != None:
        nodes_a.add(current_a)
        current_a = current_a.next
    current_b = head_b
    while current_b != None:
        if current_b in nodes_a:
            return current_b.data
        current_b = current_b.next
    return None
