from singly_linked_list import SinglyLinkedList
from doubly_linked_list import DoublyLinkedList

def demonstrate_singly_linked_list():
    print("\n=== Singly Linked List Demonstration ===")
    ll = SinglyLinkedList()
    
    # Basic operations
    print("\nAdding elements:")
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.prepend(0)
    print("List after adding 1, 2, 3 and prepending 0:")
    ll.print_list()  # Expected: 0 -> 1 -> 2 -> 3
    
    # Searching
    print("\nSearching for elements:")
    print(f"Is 2 in the list? {ll.search(2)}")  # True
    print(f"Is 5 in the list? {ll.search(5)}")  # False
    
    # Deletion
    print("\nDeleting elements:")
    ll.delete(2)
    print("List after deleting 2:")
    ll.print_list()  # Expected: 0 -> 1 -> 3
    
    # Size operations
    print(f"\nList size: {ll.get_size()}")
    print(f"Is list empty? {ll.is_empty()}")

def demonstrate_doubly_linked_list():
    print("\n=== Doubly Linked List Demonstration ===")
    dll = DoublyLinkedList()
    
    # Basic operations
    print("\nAdding elements:")
    dll.append(1)
    dll.append(2)
    dll.append(3)
    dll.prepend(0)
    print("List after adding 1, 2, 3 and prepending 0:")
    dll.print_list()  # Expected: 0 <-> 1 <-> 2 <-> 3
    
    # Demonstrate bidirectional printing
    print("\nPrinting list in reverse:")
    dll.print_list(reverse=True)  # Expected: 3 <-> 2 <-> 1 <-> 0
    
    # Searching
    print("\nSearching for elements:")
    print(f"Is 2 in the list? {dll.search(2)}")  # True
    print(f"Is 5 in the list? {dll.search(5)}")  # False
    
    # Deletion
    print("\nDeleting elements:")
    dll.delete(2)
    print("List after deleting 2:")
    dll.print_list()  # Expected: 0 <-> 1 <-> 3
    
    # Size operations
    print(f"\nList size: {dll.get_size()}")
    print(f"Is list empty? {dll.is_empty()}")

if __name__ == "__main__":
    demonstrate_singly_linked_list()
    demonstrate_doubly_linked_list()