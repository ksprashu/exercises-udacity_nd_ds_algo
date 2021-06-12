"""This program will detect loops formed within linked lists.

Exercise: Given a linked list, implement a function `iscircular`
that returns `True` if a loop exists in the list and `False` otherwise.
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, init_list=None):
        self.head = None
        if init_list:
            for value in init_list:
                self.append(value)

    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return

        # Move to the tail (the last node)
        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)
        return

##### Solution #####
def iscircular(linked_list):
    """
    Determine whether the Linked List is circular or not

    Args:
       linked_list(obj): Linked List to be checked
    Returns:
       bool: Return True if the linked list is circular, return False otherwise
    """

    # TODO: Write function to check if linked list is circular
    runner1 = runner2 = linked_list.head
    while runner1:
        if not runner1.next: return False
        if not runner2.next: return False
        if not runner2.next.next: return False

        runner1 = runner1.next
        runner2 = runner2.next.next

        if runner1 == runner2:
            return True

    return False
##### End Solution #####

list_with_loop = LinkedList([2, -1, 3, 0, 5])

# Creating a loop where the last node points back to the second node
loop_start = list_with_loop.head.next

node = list_with_loop.head
while node.next: 
    node = node.next   
node.next = loop_start

# Test Cases

# Create another circular linked list
small_loop = LinkedList([0])
small_loop.head.next = small_loop.head

print ("Pass" if iscircular(list_with_loop) else "Fail")                  # Pass
print ("Pass" if iscircular(LinkedList([-4, 7, 2, 5, -1])) else "Fail")   # Fail
print ("Pass" if iscircular(LinkedList([1])) else "Fail")                 # Fail
print ("Pass" if iscircular(small_loop) else "Fail")                      # Pass
print ("Pass" if iscircular(LinkedList([])) else "Fail")                  # Fail

