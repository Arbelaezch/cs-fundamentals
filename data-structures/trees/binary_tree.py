class TreeNode:
    """Basic node structure for binary trees."""
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    """Basic binary tree implementation."""
    def __init__(self):
        self.root = None
        self.size = 0
    
    def insert_level_order(self, data):
        """Insert data in level order (breadth-first)."""
        new_node = TreeNode(data)
        if not self.root:
            self.root = new_node
            self.size += 1
            return

        queue = [self.root]
        while queue:
            current = queue.pop(0)
            if not current.left:
                current.left = new_node
                self.size += 1
                return
            elif not current.right:
                current.right = new_node
                self.size += 1
                return
            queue.append(current.left)
            queue.append(current.right)

    def traversal_inorder(self):
        """Return list of values in inorder traversal."""
        result = []
        
        def inorder(node):
            if node:
                inorder(node.left)
                result.append(node.data)
                inorder(node.right)
                
        inorder(self.root)
        return result
    
    def traversal_preorder(self):
        """Return list of values in preorder traversal."""
        result = []
        
        def preorder(node):
            if node:
                result.append(node.data)
                preorder(node.left)
                preorder(node.right)
                
        preorder(self.root)
        return result
    
    def traversal_postorder(self):
        """Return list of values in postorder traversal."""
        result = []
        
        def postorder(node):
            if node:
                postorder(node.left)
                postorder(node.right)
                result.append(node.data)
                
        postorder(self.root)
        return result
    
    def height(self):
        """Return the height of the tree."""
        def calculate_height(node):
            if not node:
                return -1
            return 1 + max(calculate_height(node.left), calculate_height(node.right))
        
        return calculate_height(self.root)

class BinarySearchTree:
    """Binary Search Tree implementation."""
    def __init__(self):
        self.root = None
        self.size = 0
    
    def insert(self, data):
        """Insert data maintaining BST property."""
        def _insert(node, data):
            if not node:
                return TreeNode(data)
            
            if data < node.data:
                node.left = _insert(node.left, data)
            else:
                node.right = _insert(node.right, data)
            return node
        
        self.root = _insert(self.root, data)
        self.size += 1
    
    def search(self, data):
        """Search for data in the BST."""
        def _search(node, data):
            if not node or node.data == data:
                return node
            if data < node.data:
                return _search(node.left, data)
            return _search(node.right, data)
        
        return _search(self.root, data) is not None
    
    def delete(self, data):
        """Delete data from the BST."""
        def min_value_node(node):
            current = node
            while current.left:
                current = current.left
            return current
        
        def _delete(node, data):
            if not node:
                return node
            
            if data < node.data:
                node.left = _delete(node.left, data)
            elif data > node.data:
                node.right = _delete(node.right, data)
            else:
                if not node.left:
                    return node.right
                elif not node.right:
                    return node.left
                
                # Node with two children
                successor = min_value_node(node.right)
                node.data = successor.data
                node.right = _delete(node.right, successor.data)
            
            return node
        
        if self.search(data):
            self.root = _delete(self.root, data)
            self.size -= 1
            return True
        return False
    
    def traversal_inorder(self):
        """Return sorted list of values (inorder traversal)."""
        result = []
        
        def inorder(node):
            if node:
                inorder(node.left)
                result.append(node.data)
                inorder(node.right)
                
        inorder(self.root)
        return result