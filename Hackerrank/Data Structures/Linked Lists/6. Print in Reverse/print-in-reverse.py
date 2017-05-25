"""
 Print elements of a linked list in reverse order as standard output
 head could be None as well for empty list
 Node is defined as

 class Node(object):

   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node


"""

def ReversePrint(head):
    data = []
    if head == None:
        return
    while head != None:
        data.insert(0,head.data)
        head = head.next
    for d in data:
        print(d)
