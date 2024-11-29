class CircularArray:
    """A circular array implementation."""
    
    def __init__(self, capacity=8):
        self.capacity = capacity
        self.size = 0
        self.front = 0  # Index of the first element
        self.array = [None] * capacity
    
    def enqueue(self, item):
        """Add an item to the end of the array. O(1) time complexity."""
        if self.size == self.capacity:
            self._resize(2 * self.capacity)
            
        rear = (self.front + self.size) % self.capacity
        self.array[rear] = item
        self.size += 1
    
    def dequeue(self):
        """Remove and return the first item. O(1) time complexity."""
        if self.is_empty():
            raise IndexError("Array is empty")
            
        item = self.array[self.front]
        self.array[self.front] = None
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        
        if self.size <= self.capacity // 4:
            self._resize(self.capacity // 2)
            
        return item
    
    def _resize(self, new_capacity):
        """Resize the circular array."""
        new_array = [None] * new_capacity
        for i in range(self.size):
            new_array[i] = self.array[(self.front + i) % self.capacity]
        self.array = new_array
        self.capacity = new_capacity
        self.front = 0
    
    def get(self, index):
        """Get item at index relative to front. O(1) time complexity."""
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds")
        return self.array[(self.front + index) % self.capacity]
    
    def length(self):
        """Return the number of items in the array. O(1) time complexity."""
        return self.size
    
    def is_empty(self):
        """Check if the array is empty. O(1) time complexity."""
        return self.size == 0
    
    def print_array(self):
        """Print all elements in the array."""
        elements = []
        for i in range(self.size):
            elements.append(str(self.get(i)))
        print("[" + ", ".join(elements) + "]")