class ArrayQueue:
    """Queue implementation using a dynamic array."""
    def __init__(self):
        self.items = []
    
    def enqueue(self, item):
        """Add an item to the end of the queue. O(1) amortized time complexity."""
        self.items.append(item)
    
    def dequeue(self):
        """Remove and return the front item. O(n) time complexity."""
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.items.pop(0)
    
    def front(self):
        """Return the front item without removing it. O(1) time complexity."""
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.items[0]
    
    def is_empty(self):
        """Check if the queue is empty. O(1) time complexity."""
        return len(self.items) == 0
    
    def size(self):
        """Return the number of items in the queue. O(1) time complexity."""
        return len(self.items)
    
    def print_queue(self):
        """Print the queue from front to back."""
        print("Front ->", end=" ")
        print(" -> ".join(str(x) for x in self.items))

class LinkedQueue:
    """Queue implementation using a linked list."""
    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None
    
    def __init__(self):
        self.front = None
        self.rear = None
        self._size = 0
    
    def enqueue(self, item):
        """Add an item to the end of the queue. O(1) time complexity."""
        new_node = self.Node(item)
        if self.is_empty():
            self.front = new_node
        else:
            self.rear.next = new_node
        self.rear = new_node
        self._size += 1
    
    def dequeue(self):
        """Remove and return the front item. O(1) time complexity."""
        if self.is_empty():
            raise IndexError("Queue is empty")
        item = self.front.data
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        self._size -= 1
        return item
    
    def front_item(self):
        """Return the front item without removing it. O(1) time complexity."""
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.front.data
    
    def is_empty(self):
        """Check if the queue is empty. O(1) time complexity."""
        return self.front is None
    
    def size(self):
        """Return the number of items in the queue. O(1) time complexity."""
        return self._size
    
    def print_queue(self):
        """Print the queue from front to back."""
        print("Front ->", end=" ")
        current = self.front
        elements = []
        while current:
            elements.append(str(current.data))
            current = current.next
        print(" -> ".join(elements))