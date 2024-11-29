from dynamic_array import DynamicArray, CircularArray

def demonstrate_dynamic_array():
    print("\n=== Dynamic Array Demonstration ===")
    arr = DynamicArray()
    
    # Basic operations
    print("\nAppending elements:")
    arr.append(1)
    arr.append(2)
    arr.append(3)
    print("Array after appending 1, 2, 3:")
    arr.print_array()
    
    # Insertion
    print("\nInserting element:")
    arr.insert(1, 5)
    print("Array after inserting 5 at index 1:")
    arr.print_array()
    
    # Removal
    print("\nRemoving element:")
    arr.remove(1)
    print("Array after removing element at index 1:")
    arr.print_array()
    
    # Access and modification
    print("\nAccessing and modifying elements:")
    print(f"Element at index 1: {arr.get(1)}")
    arr.set(1, 10)
    print("Array after setting index 1 to 10:")
    arr.print_array()
    
    # Size operations
    print(f"\nArray length: {arr.length()}")
    print(f"Is array empty? {arr.is_empty()}")

def demonstrate_circular_array():
    print("\n=== Circular Array Demonstration ===")
    carr = CircularArray()
    
    # Enqueue operations
    print("\nEnqueuing elements:")
    for i in range(1, 6):
        carr.enqueue(i)
    print("Array after enqueuing 1 through 5:")
    carr.print_array()
    
    # Dequeue operations
    print("\nDequeuing elements:")
    print(f"Dequeued: {carr.dequeue()}")
    print(f"Dequeued: {carr.dequeue()}")
    print("Array after dequeuing two elements:")
    carr.print_array()
    
    # Enqueue after dequeue
    print("\nEnqueuing more elements:")
    carr.enqueue(6)
    carr.enqueue(7)
    print("Array after enqueuing 6 and 7:")
    carr.print_array()
    
    # Size operations
    print(f"\nArray length: {carr.length()}")
    print(f"Is array empty? {carr.is_empty()}")

if __name__ == "__main__":
    demonstrate_dynamic_array()
    demonstrate_circular_array()