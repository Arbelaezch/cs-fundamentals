from stack import ArrayStack, LinkedStack
from queue import ArrayQueue, LinkedQueue

def demonstrate_stacks():
    print("\n=== Stack Demonstrations ===")
    
    # Array-based Stack
    print("\nArray-based Stack:")
    array_stack = ArrayStack()
    
    print("Pushing elements: 1, 2, 3")
    array_stack.push(1)
    array_stack.push(2)
    array_stack.push(3)
    array_stack.print_stack()
    
    print(f"Stack size: {array_stack.size()}")
    print(f"Top element: {array_stack.peek()}")
    
    print("Popping two elements")
    print(f"Popped: {array_stack.pop()}")
    print(f"Popped: {array_stack.pop()}")
    array_stack.print_stack()
    
    # Linked List-based Stack
    print("\nLinked List-based Stack:")
    linked_stack = LinkedStack()
    
    print("Pushing elements: 1, 2, 3")
    linked_stack.push(1)
    linked_stack.push(2)
    linked_stack.push(3)
    linked_stack.print_stack()
    
    print(f"Stack size: {linked_stack.size()}")
    print(f"Top element: {linked_stack.peek()}")
    
    print("Popping two elements")
    print(f"Popped: {linked_stack.pop()}")
    print(f"Popped: {linked_stack.pop()}")
    linked_stack.print_stack()

def demonstrate_queues():
    print("\n=== Queue Demonstrations ===")
    
    # Array-based Queue
    print("\nArray-based Queue:")
    array_queue = ArrayQueue()
    
    print("Enqueuing elements: 1, 2, 3")
    array_queue.enqueue(1)
    array_queue.enqueue(2)
    array_queue.enqueue(3)
    array_queue.print_queue()
    
    print(f"Queue size: {array_queue.size()}")
    print(f"Front element: {array_queue.front()}")
    
    print("Dequeuing two elements")
    print(f"Dequeued: {array_queue.dequeue()}")
    print(f"Dequeued: {array_queue.dequeue()}")
    array_queue.print_queue()
    
    # Linked List-based Queue
    print("\nLinked List-based Queue:")
    linked_queue = LinkedQueue()
    
    print("Enqueuing elements: 1, 2, 3")
    linked_queue.enqueue(1)
    linked_queue.enqueue(2)
    linked_queue.enqueue(3)
    linked_queue.print_queue()
    
    print(f"Queue size: {linked_queue.size()}")
    print(f"Front element: {linked_queue.front_item()}")
    
    print("Dequeuing two elements")
    print(f"Dequeued: {linked_queue.dequeue()}")
    print(f"Dequeued: {linked_queue.dequeue()}")
    linked_queue.print_queue()

if __name__ == "__main__":
    demonstrate_stacks()
    demonstrate_queues()