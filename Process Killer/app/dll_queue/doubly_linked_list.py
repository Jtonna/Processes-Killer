""" Each ListNode holds a reference to its previous node
    as well as its next node in the list."""

class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """ Wrap the given value in the ListNode and
        insert it AFTER this node.
        note: this node could already be pointing to a next node """
    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """ Wrap the given value in the ListNode and
        insert it BEFORE this node.
        note: this node could already be pointing to a next node """
    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev
    
    """ Rearranges this ListNodes previous and next pointers accordingly;
        effectively deleing this ListNode. """
    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev
    
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0
    
    """ Returns the length of the DoublyLinkedList"""
    def ___len___(self):
        return self.length
    
    """ Wraps the given value in a ListNode
       then inserts it as the new head of the list"""
    def add_to_head(self, value):
        new_node = ListNode(value)
        self.length += 1

        # If we dont have a head or a tail we need to create the start of the DLL
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
        # If there is something on the head of the DLL, we need to insert the new_node at the beginning & re-assignt he original head to next
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
            


    """ Removes the DoublyLinkedLists current head node
        this in turn makes the 'next' node the new head of the list"""
    def remove_from_head(self):
        pass

    """ """
    def add_to_tail(self, value):
        pass

    """ """
    def remove_from_tail(self):
        pass

    