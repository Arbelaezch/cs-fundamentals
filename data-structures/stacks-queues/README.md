# Stacks and Queues

## Overview
Stacks and queues are fundamental abstract data types that follow specific patterns for adding and removing elements. This implementation provides both array-based and linked list-based versions of each data structure.


## Stack
A stack is a Last-In-First-Out (LIFO) data structure with two primary operations:
- **Push**: Add an element to the top
- **Pop**: Remove the top element

### Key Operations
- Push: Add to top
- Pop: Remove from top
- Peek: View top element
- IsEmpty: Check if stack is empty
- Size: Get number of elements

### Common Use Cases
1. Function call stack
2. Expression evaluation
3. Undo/Redo operations
4. Browser history
5. Syntax parsing


## Queue
A queue is a First-In-First-Out (FIFO) data structure with two primary operations:
- **Enqueue**: Add an element to the back
- **Dequeue**: Remove the front element

### Key Operations
- Enqueue: Add to back
- Dequeue: Remove from front
- Front: View front element
- IsEmpty: Check if queue is empty
- Size: Get number of elements

### Common Use Cases
1. Task scheduling
2. Print queue
3. Breadth-first search
4. Message queues
5. CPU scheduling

## Implementations

### Array-based Implementation
- Uses dynamic array (Python list)
- Memory contiguous
- Better cache performance
- May require resizing

### Linked List-based Implementation
- Uses linked nodes
- Dynamic memory allocation
- No resizing required
- Extra memory for node references

## Time Complexity

| Operation | Stack (Both Impl.) | Array Queue | Linked Queue |
|-----------|-------------------|-------------|--------------|
| Push/Enqueue      | O(1)*     | O(1)*       | O(1) |
| Pop/Dequeue       | O(1)      | O(n)        | O(1) |
| Peek/Front        | O(1)      | O(1)        | O(1) |
| IsEmpty           | O(1)      | O(1)        | O(1) |
| Size              | O(1)      | O(1)        | O(1) |

*Amortized time complexity for array-based implementations
