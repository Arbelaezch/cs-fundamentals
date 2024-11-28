# Linked Lists

## Conceptual Overview
A linked list is a linear data structure where each element points to the next element in the sequence. Unlike arrays, linked lists do not store elements in contiguous memory locations. Instead, each element (node) contains both data and a reference to the next node in the sequence.

## Types of Linked Lists
1. **Singly Linked List**
   - Each node points to the next node
   - Last node points to null
   - Only forward traversal is possible

2. **Doubly Linked List**
   - Each node has references to both next and previous nodes
   - Allows bidirectional traversal
   - Takes more memory due to extra reference

3. **Circular Linked List**
   - Last node points back to the first node
   - Can be either singly or doubly linked

## Visual Representation
```
Singly Linked List:
[Data|Next] -> [Data|Next] -> [Data|Next] -> null

Doubly Linked List:
null <- [Prev|Data|Next] <-> [Prev|Data|Next] <-> [Prev|Data|Next] -> null
```

## Operations and Time Complexity
| Operation       | Time Complexity | Description |
|----------------|-----------------|-------------|
| Access         | O(n)           | Must traverse from head |
| Insert at Head | O(1)           | Constant time operation |
| Insert at Tail | O(n)           | Must traverse to end |
| Delete at Head | O(1)           | Constant time operation |
| Delete at Tail | O(n)           | Must traverse to end |
| Search         | O(n)           | Must traverse list |

## Space Complexity
- O(n) where n is the number of elements
- Extra space per node for next/previous pointers

## Common Use Cases
1. **Implementation of Other Data Structures**
   - Stacks and Queues
   - Hash Tables (chaining)
   - Adjacency Lists for Graphs

2. **System Design**
   - Implementation of file systems
   - Memory allocation
   - Task scheduling

## Advantages and Disadvantages
### Advantages
- Dynamic size
- Efficient insertion/deletion at beginning
- No pre-allocation of space
- Memory efficiency when size is unknown

### Disadvantages
- No random access
- Extra memory for pointers
- Not cache-friendly
- Reverse traversal difficult (in singly linked lists)

## Implementation Details
### Node Structure
```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
```

### Key Methods
- `append(data)` - Add to end
- `prepend(data)` - Add to beginning
- `delete(data)` - Remove first occurrence
- `search(data)` - Find element

See implementation in [singly_linked_list.py](./singly_linked_list.py)

## Real-world Applications
1. **Music Player Playlists**
   - Next/previous song functionality
   - Dynamic addition/removal of songs

2. **Browser History**
   - Forward/backward navigation
   - New page visits

3. **Text Editors**
   - Undo/redo functionality
   - Line management

## Common Interview Questions
1. How to detect a cycle in a linked list?
2. How to find the middle element?
3. How to reverse a linked list?
4. How to merge two sorted linked lists?

## Related Data Structures
- Doubly Linked Lists
- Circular Linked Lists
- Skip Lists

## How to Run
```bash
python examples.py
```
