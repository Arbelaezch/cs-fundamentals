# Arrays

## Overview
Arrays are fundamental data structures that store elements in contiguous memory locations. This implementation focuses on dynamic arrays (similar to Python's built-in list) and circular arrays, demonstrating how these data structures work under the hood.

## Types of Arrays
### Dynamic Array
- Automatically resizes when capacity is reached
- Provides amortized O(1) time complexity for appends
- Implements the resizing strategy used by many modern programming languages

### Circular Array
- Fixed-size array viewed as circular
- Efficient for queue operations
- Useful for buffering and scheduling algorithms

## Implementation Details

### Dynamic Array
- Initial capacity: 2 elements
- Growth factor: 2x when full
- Shrink factor: 0.25x when quarter full
- Amortized O(1) append operations

### Circular Array
- Uses modular arithmetic for wraparound
- Maintains front pointer
- Efficient enqueue/dequeue operations

## Time Complexity

| Operation | Dynamic Array | Circular Array |
|-----------|---------------|----------------|
| Append/Enqueue | O(1)* | O(1) |
| Insert | O(n) | - |
| Remove | O(n) | O(1) (dequeue) |
| Access | O(1) | O(1) |
| Search | O(n) | O(n) |

*Amortized time complexity

## Space Complexity
- O(n) where n is the number of elements
- Extra space used during resizing operations
- Memory usage optimized through shrinking

## Common Operations
1. **Append/Enqueue**
   ```python
   arr.append(item)      # Dynamic Array
   carr.enqueue(item)    # Circular Array
   ```

2. **Access**
   ```python
   item = arr.get(index)
   ```

3. **Insert**
   ```python
   arr.insert(index, item)
   ```

4. **Remove**
   ```python
   arr.remove(index)     # Dynamic Array
   item = carr.dequeue() # Circular Array
   ```

## Real-world Applications
1. **Dynamic Arrays**
   - Implementation of list-like structures
   - Building blocks for other data structures
   - Buffer management

2. **Circular Arrays**
   - Audio/Video buffers
   - Task scheduling
   - Memory management
   - Network packet processing

## Advanced Concepts
1. **Amortized Analysis**
   - Cost of resizing operations
   - Growth factor selection
   - Memory-time tradeoffs

2. **Memory Management**
   - Contiguous allocation
   - Fragmentation handling
   - Cache efficiency