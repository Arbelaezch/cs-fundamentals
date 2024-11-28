class Node:
    """A node in a singly linked list."""
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    """Implementation of a singly linked list with core operations."""
    def __init__(self):
        self.head = None
        self.size = 0
    
    def append(self, data):
        """Add a new node to the end of the list. O(n) time complexity."""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        self.size += 1
    
    def prepend(self, data):
        """Add a new node to the start of the list. O(1) time complexity."""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.size += 1
    
    def delete(self, data):
        """Delete the first occurrence of data in the list. O(n) time complexity."""
        if not self.head:
            return

        if self.head.data == data:
            self.head = self.head.next
            self.size -= 1
            return

        current = self.head
        while current.next and current.next.data != data:
            current = current.next

        if current.next:
            current.next = current.next.next
            self.size -= 1
    
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
    
    def print_list(self):
        """Print all elements in the list. O(n) time complexity."""
        elements = []
        current = self.head
        while current:
            elements.append(str(current.data))
            current = current.next
        print(" -> ".join(elements))