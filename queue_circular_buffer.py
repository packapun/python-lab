from typing import Optional, List

class Queue:
    """
    A queue implementation with fixed capacity using circular buffer.
    
    Supports FIFO (First In, First Out) operations with O(1) time complexity
    for enqueue, dequeue, and peek operations. Stores integers only.
    """
    
    def __init__(self, capacity: int) -> None:
        """
        Initialize queue with given capacity.
        
        Args:
            capacity: Maximum number of elements the queue can hold
            
        Raises:
            ValueError: If capacity is not positive
        """
        if capacity <= 0:
            raise ValueError("Capacity must be positive")
        
        self.capacity = capacity
        self._items: List[Optional[int]] = [None] * capacity
        self._front = 0  # Index of front element
        self._rear = 0   # Index where next element will be inserted
        self._size = 0   # Current number of elements
    
    def is_empty(self) -> bool:
        """Check if queue is empty."""
        return self._size == 0
    
    def is_full(self) -> bool:
        """Check if queue is at capacity."""
        return self._size == self.capacity
    
    def size(self) -> int:
        """Return current number of elements in queue."""
        return self._size
    
    def enqueue(self, item: int) -> None:
        """
        Add item to rear of queue.
        
        Args:
            item: Integer to add to queue
            
        Raises:
            OverflowError: If queue is full
        """
        if self.is_full():
            raise OverflowError("Cannot enqueue to full queue")
        
        self._items[self._rear] = item
        self._rear = (self._rear + 1) % self.capacity  # Circular increment
        self._size += 1
    
    def dequeue(self) -> int:
        """
        Remove and return front element from queue.
        
        Returns:
            The front element of the queue
            
        Raises:
            IndexError: If queue is empty
        """
        if self.is_empty():
            raise IndexError("Cannot dequeue from empty queue")
        
        item = self._items[self._front]
        self._items[self._front] = None  # Clear reference
        self._front = (self._front + 1) % self.capacity  # Circular increment
        self._size -= 1
        return item
    
    def peek(self) -> int:
        """
        Return front element without removing it.
        
        Returns:
            The front element of the queue
            
        Raises:
            IndexError: If queue is empty
        """
        if self.is_empty():
            raise IndexError("Cannot peek at empty queue")
        return self._items[self._front]
    
    # Alias for peek() - common in interviews
    def front(self) -> int:
        """Alias for peek()."""
        return self.peek()
    
    def rear(self) -> int:
        """
        Return rear element without removing it.
        
        Returns:
            The rear element of the queue
            
        Raises:
            IndexError: If queue is empty
        """
        if self.is_empty():
            raise IndexError("Cannot access rear of empty queue")
        # Rear index points to next insertion, so we need previous index
        rear_index = (self._rear - 1) % self.capacity
        return self._items[rear_index]
    
    def __len__(self) -> int:
        """Return size of queue (enables len() function)."""
        return self._size
    
    def __str__(self) -> str:
        """String representation of queue from front to rear."""
        if self.is_empty():
            return "Queue([], capacity={})".format(self.capacity)
        
        elements = []
        current = self._front
        for _ in range(self._size):
            elements.append(self._items[current])
            current = (current + 1) % self.capacity
        
        return f"Queue({elements}, capacity={self.capacity})"
    
    def __repr__(self) -> str:
        """Developer-friendly representation."""
        return f"Queue(capacity={self.capacity}, size={self._size}, front={self._front}, rear={self._rear})"


# Alternative implementation using collections.deque (more Pythonic)
from collections import deque

class SimpleQueue:
    """
    A simpler queue implementation using collections.deque.
    
    This is more Pythonic but doesn't have fixed capacity.
    Good to mention in interviews as an alternative. Stores integers only.
    """
    
    def __init__(self, maxsize: Optional[int] = None) -> None:
        """
        Initialize queue with optional maximum size.
        
        Args:
            maxsize: Maximum number of elements (None for unlimited)
        """
        self.maxsize = maxsize
        self._items: deque[int] = deque()
    
    def is_empty(self) -> bool:
        """Check if queue is empty."""
        return len(self._items) == 0
    
    def is_full(self) -> bool:
        """Check if queue is at capacity."""
        return self.maxsize is not None and len(self._items) >= self.maxsize
    
    def size(self) -> int:
        """Return current number of elements in queue."""
        return len(self._items)
    
    def enqueue(self, item: int) -> None:
        """Add integer to rear of queue."""
        if self.is_full():
            raise OverflowError("Cannot enqueue to full queue")
        self._items.append(item)
    
    def dequeue(self) -> int:
        """Remove and return front element from queue."""
        if self.is_empty():
            raise IndexError("Cannot dequeue from empty queue")
        return self._items.popleft()
    
    def peek(self) -> int:
        """Return front element without removing it."""
        if self.is_empty():
            raise IndexError("Cannot peek at empty queue")
        return self._items[0]
    
    def __len__(self) -> int:
        return len(self._items)
    
    def __str__(self) -> str:
        return f"SimpleQueue({list(self._items)}, maxsize={self.maxsize})"


# Example usage and test cases
if __name__ == "__main__":
    print("=== Circular Buffer Queue ===")
    queue = Queue(4)
    
    print(f"Empty queue: {queue.is_empty()}")  # True
    print(f"Queue size: {len(queue)}")  # 0
    
    # Enqueue elements
    for i in range(1, 5):
        queue.enqueue(i)
        print(f"Enqueued {i}: {queue}")
    
    print(f"Full queue: {queue.is_full()}")  # True
    print(f"Front element: {queue.peek()}")  # 1
    print(f"Rear element: {queue.rear()}")   # 4
    
    # Dequeue some elements
    for _ in range(2):
        dequeued = queue.dequeue()
        print(f"Dequeued {dequeued}: {queue}")
    
    # Add more elements to show circular behavior
    queue.enqueue(5)
    queue.enqueue(6)
    print(f"After adding 5,6: {queue}")
    
    # Dequeue all remaining
    while not queue.is_empty():
        dequeued = queue.dequeue()
        print(f"Dequeued {dequeued}, size: {queue.size()}")
    
    print("\n=== Simple Queue (using deque) ===")
    simple_queue = SimpleQueue(3)
    
    for item in [10, 20, 30]:
        simple_queue.enqueue(item)
        print(f"Enqueued {item}: {simple_queue}")
    
    while not simple_queue.is_empty():
        dequeued = simple_queue.dequeue()
        print(f"Dequeued {dequeued}: {simple_queue}")
    
    # Error handling examples
    try:
        queue.dequeue()  # Should raise IndexError
    except IndexError as e:
        print(f"Error: {e}")
    
    try:
        queue = Queue(0)  # Should raise ValueError
    except ValueError as e:
        print(f"Error: {e}")
