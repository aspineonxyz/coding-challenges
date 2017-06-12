def insert(self, head, data):
    current = head
    if current != None:
        while current.next:
            current = current.next
        tmp = Node(data)
        current.next = tmp
        return head
    else:
        current = Node(data)
        return current
