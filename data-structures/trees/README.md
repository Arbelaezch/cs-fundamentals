# Binary Trees and Binary Search Trees

## Overview
Binary trees are hierarchical data structures where each node has at most two children, referred to as the left child and right child. This implementation includes both a basic binary tree and a binary search tree (BST).

## Types of Binary Trees

### Basic Binary Tree
- Each node has at most two children
- No specific ordering of elements
- Used for hierarchical data representation

### Binary Search Tree (BST)
- Special type of binary tree
- Left subtree contains only nodes with values less than the parent
- Right subtree contains only nodes with values greater than the parent
- No duplicate values (in this implementation)

## Tree Traversals

### Inorder (Left-Root-Right)
- Visit left subtree
- Visit root
- Visit right subtree
- Gives sorted order for BST

### Preorder (Root-Left-Right)
- Visit root
- Visit left subtree
- Visit right subtree
- Useful for copying/serializing tree

### Postorder (Left-Right-Root)
- Visit left subtree
- Visit right subtree
- Visit root
- Useful for deletion and expression evaluation

## Binary Search Tree Properties
- Efficient searching, insertion, and deletion
- Maintains sorted order
- Average case O(log n) operations
- Can degenerate to O(n) in worst case

## Operations and Time Complexity

| Operation     | Binary Tree | BST (Average) | BST (Worst) |
|--------------|-------------|---------------|-------------|
| Insertion    | O(n)        | O(log n)      | O(n)        |
| Deletion     | O(n)        | O(log n)      | O(n)        |
| Search       | O(n)        | O(log n)      | O(n)        |
| Traversal    | O(n)        | O(n)          | O(n)        |

## Common Use Cases

### Binary Trees
1. File system hierarchies
2. HTML/XML parsing
3. Decision trees
4. Game trees

### Binary Search Trees
1. Symbol tables
2. Database indexing
3. Priority queues
4. Expression parsers

## Implementation Details

### Node Structure
```python
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
```

### Key Methods
- insert/insert_level_order
- search (BST)
- delete (BST)
- traversal methods (inorder, preorder, postorder)
- height calculation

## Examples
See [examples.py](examples.py) for detailed usage demonstrations including:
- Tree creation and manipulation
- All types of traversals
- Search and deletion operations
- Visual representation of tree structures