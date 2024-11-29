from binary_tree import BinaryTree, BinarySearchTree

def demonstrate_binary_tree():
    print("\n=== Binary Tree Demonstration ===")
    bt = BinaryTree()
    
    # Insert values in level order
    print("\nInserting values 1-7 in level order:")
    for i in range(1, 8):
        bt.insert_level_order(i)
    
    print("\nTree Traversals:")
    print(f"Inorder (Left-Root-Right):   {bt.traversal_inorder()}")
    print(f"Preorder (Root-Left-Right):  {bt.traversal_preorder()}")
    print(f"Postorder (Left-Right-Root): {bt.traversal_postorder()}")
    
    print(f"\nTree Height: {bt.height()}")
    print(f"Tree Size: {bt.size}")

def demonstrate_binary_search_tree():
    print("\n=== Binary Search Tree Demonstration ===")
    bst = BinarySearchTree()
    
    # Insert values
    values = [5, 3, 7, 2, 4, 6, 8]
    print(f"\nInserting values: {values}")
    for value in values:
        bst.insert(value)
    
    # Show sorted order
    print(f"Inorder traversal (sorted): {bst.traversal_inorder()}")
    
    # Demonstrate search
    print("\nSearch operations:")
    print(f"Search for 6: {bst.search(6)}")
    print(f"Search for 9: {bst.search(9)}")
    
    # Demonstrate deletion
    print("\nDeletion operations:")
    print(f"Delete 3 (node with two children): {bst.delete(3)}")
    print(f"New inorder traversal: {bst.traversal_inorder()}")
    
    print(f"Delete 8 (leaf node): {bst.delete(8)}")
    print(f"New inorder traversal: {bst.traversal_inorder()}")
    
    print(f"\nTree Size: {bst.size}")

def visual_tree_example():
    """
    Creates and prints a visual representation of a simple binary tree
    using ASCII characters.
    """
    print("\n=== Visual Tree Example ===")
    bt = BinaryTree()
    for i in range(1, 8):
        bt.insert_level_order(i)
    
    print("""
    Binary Tree (level-order insertion of 1-7):
    
           1
         /   \\
        2     3
       / \\   / \\
      4   5 6   7
    
    Binary Search Tree (insertion of 5,3,7,2,4,6,8):
    
           5
         /   \\
        3     7
       / \\   / \\
      2   4 6   8
    """)

if __name__ == "__main__":
    demonstrate_binary_tree()
    demonstrate_binary_search_tree()
    visual_tree_example()