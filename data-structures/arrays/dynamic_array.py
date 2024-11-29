class DynamicArray:
    """A dynamic array implementation similar to Python's list."""
    
    def __init__(self, capacity=2):
        self.capacity = capacity
        self.size = 0
        # Initialize underlying static array
        self.array = [None] * capacity
    
    def append(self, item):
        """Add an element to the end of the array. Amortized O(1) time complexity."""
        if self.size == self.capacity:
            self._resize(2 * self.capacity)
        
        self.array[self.size] = item
        self.size += 1
    
    def insert(self, index, item):
        """Insert an item at a specific index. O(n) time complexity."""
        if index < 0 or index > self.size:
            raise IndexError("Index out of bounds")
            
        if self.size == self.capacity:
            self._resize(2 * self.capacity)
            
        # Shift elements to the right
        for i in range(self.size, index, -1):
            self.array[i] = self.array[i-1]
            
        self.array[index] = item
        self.size += 1
    
    def remove(self, index):
        """Remove item at index. O(n) time complexity."""
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds")
            
        # Shift elements to the left
        for i in range(index, self.size - 1):
            self.array[i] = self.array[i + 1]
            
        self.size -= 1
        
        # Shrink array if it's too empty
        if self.size <= self.capacity // 4:
            self._resize(self.capacity // 2)
    
    def _resize(self, new_capacity):
        """Resize the underlying array to the new capacity."""
        new_array = [None] * new_capacity
        for i in range(self.size):
            new_array[i] = self.array[i]
        self.array = new_array
        self.capacity = new_capacity
    
    def get(self, index):
        """Get item at index. O(1) time complexity."""
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds")
        return self.array[index]
    
    def set(self, index, item):
        """Set item at index. O(1) time complexity."""
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds")
        self.array[index] = item
    
    def length(self):
        """Return the number of items in the array. O(1) time complexity."""
        return self.size
    
    def is_empty(self):
        """Check if the array is empty. O(1) time complexity."""
        return self.size == 0
    
    def print_array(self):
        """Print all elements in the array."""
        elements = [str(self.array[i]) for i in range(self.size)]
        print("[" + ", ".join(elements) + "]")