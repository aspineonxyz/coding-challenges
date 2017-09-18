# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):

    def itol(self, num):
        """Converts an Integer to a Singly-linked list representation.

        Args:
            num: An Integer to be converted.

        Returns:
            head: The head node of a Singly-linked list representation of the Integer argument passed.
        """
        num_str = str(num)[::-1]
        head = ListNode(num_str[0:1])
        num_str = num_str[1:]
        current_node = head
        while num_str != '':
            node = ListNode(num_str[0:1])
            current_node.next = node
            current_node = current_node.next
            num_str = num_str[1:]
        return head


    def ltoi(self, head):
        """Converts a Singly-linked list to an Integer.

        Args:
            head: A Singly-linked list.

        Returns:
            num: An Integer converted from the Singly-linked list.

        Raises:
            TypeError: An error occured accessing the value stored in the node as it is not an Integer.
        """
        num = 0
        mantissa = 1
        current_node = head
        while current_node != None:
            if isinstance(current_node.val, int):
                num += (current_node.val * mantissa)
                mantissa *= 10
                current_node = current_node.next
            else:
                raise TypeError('Singly-linked list must only store Integer values to be converted')
        return num


    def addTwoNumbers(self, l1, l2):
        """Add two numbers stored in Singly-linked list representations together and return the result in a Singly-linked list.

        Args:
            l1: A Singly-linked list representation of the left addend.
            l2: A Singly-linked list representation of the right addend.

        Returns:
            ListNode: a Singly-linked list representation of the addtion of the two numbers stored in the linked list arguments.
        """
        return self.itol(self.ltoi(l1) + self.ltoi(l2))
