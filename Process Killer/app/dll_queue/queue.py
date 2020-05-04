from .doubly_linked_list import DoublyLinkedList

#  A queue is first in -> first out.


class Queue:
    def __init__(self):
        self.size = 0
        self.storage = DoublyLinkedList()

    def enqueue(self, value):
        self.size += 1

        # Case: Storage head is None
        if self.storage.head is None:
            # TODO: Logger for enqueue @ head
            #print(f"     adding '{value}' to head")
            self.storage.add_to_head(value)
        # Case: The head is not None
        else:
            # TODO: Logger for enqueue @ tail
            #print(f"     adding '{value}' to tail")
            self.storage.add_to_tail(value)

    def dequeue(self):
        # Case: Queue is empty
        if self.size == 0:
            return
        # Case: Queue has data
        else:
            self.size -= 1
            #  We need to store the value elsewhere to prevent it from being modified by +1 so we can return it later
            head_true_value = self.storage.head.value
            self.storage.remove_from_head()

            # TODO: Logger for dequeue
            #print(f"     removing '{head_true_value}' from head")
            return head_true_value

    def len(self):
        return self.size
