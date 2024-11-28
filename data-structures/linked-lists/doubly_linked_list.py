class Node:
    """A node in a doubly linked list."""
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    """Implementation of a doubly linked list with core operations."""
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def append(self, data):
        """Add a new node to the end of the list. O(1) time complexity."""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1
    
    def prepend(self, data):
        """Add a new node to the start of the list. O(1) time complexity."""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.size += 1
    
    def delete(self, data):
        """Delete the first occurrence of data in the list. O(n) time complexity."""
        current = self.head
        while current:
            if current.data == data:
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next

                if current.next:
                    current.next.prev = current.prev
                else:
                    self.tail = current.prev

                self.size -= 1
                return
            current = current.next
    
    def search(self, data):
        """Search for data in the list. O(n) time complexity."""
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False
    
    def get_size(self):
        """Return the size of the list. O(1) time complexity."""
        return self.size
    
    def is_empty(self):
        """Check if the list is empty. O(1) time complexity."""
        return self.size == 0
    
    def print_list(self, reverse=False):
        """Print all elements in the list. O(n) time complexity."""
        elements = []
        current = self.tail if reverse else self.head
        while current:
            elements.append(str(current.data))
            current = current.prev if reverse else current.next
        print(" <-> ".join(elements))