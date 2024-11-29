class ArrayStack:
    """Stack implementation using a dynamic array."""
    def __init__(self):
        self.items = []
    
    def push(self, item):
        """Add an item to the top of the stack. O(1) amortized time complexity."""
        self.items.append(item)
    
    def pop(self):
        """Remove and return the top item. O(1) time complexity."""
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.items.pop()
    
    def peek(self):
        """Return the top item without removing it. O(1) time complexity."""
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.items[-1]
    
    def is_empty(self):
        """Check if the stack is empty. O(1) time complexity."""
        return len(self.items) == 0
    
    def size(self):
        """Return the number of items in the stack. O(1) time complexity."""
        return len(self.items)
    
    def print_stack(self):
        """Print the stack from top to bottom."""
        print("Top ->", end=" ")
        print(" -> ".join(str(x) for x in reversed(self.items)))

class LinkedStack:
    """Stack implementation using a linked list."""
    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None
    
    def __init__(self):
        self.top = None
        self._size = 0
    
    def push(self, item):
        """Add an item to the top of the stack. O(1) time complexity."""
        new_node = self.Node(item)
        new_node.next = self.top
        self.top = new_node
        self._size += 1
    
    def pop(self):
        """Remove and return the top item. O(1) time complexity."""
        if self.is_empty():
            raise IndexError("Stack is empty")
        item = self.top.data
        self.top = self.top.next
        self._size -= 1
        return item
    
    def peek(self):
        """Return the top item without removing it. O(1) time complexity."""
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.top.data
    
    def is_empty(self):
        """Check if the stack is empty. O(1) time complexity."""
        return self.top is None
    
    def size(self):
        """Return the number of items in the stack. O(1) time complexity."""
        return self._size
    
    def print_stack(self):
        """Print the stack from top to bottom."""
        print("Top ->", end=" ")
        current = self.top
        elements = []
        while current:
            elements.append(str(current.data))
            current = current.next
        print(" -> ".join(elements))