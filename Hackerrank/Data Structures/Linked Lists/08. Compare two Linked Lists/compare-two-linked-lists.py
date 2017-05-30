"""
 Merge two linked list
 head could be None as well for empty list
 Node is defined as

 class Node(object):

   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method.
"""

def CompareLists(headA, headB):
    if headA == None and headB == None:
        return 1
    while headA != None or headB != None:
        try:
            if headA.data != headB.data:
                return 0
            headA = headA.next
            headB = headB.next
        except AttributeError:
            return 0
    return 1
