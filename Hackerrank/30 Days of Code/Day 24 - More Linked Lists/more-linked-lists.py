def removeDuplicates(self,head):
    if head == None:
        return None
    current_node = head
    while current_node.next:
        if current_node.data == current_node.next.data:
            current_node.next = current_node.next.next
        else:
            current_node = current_node.next
    return head
