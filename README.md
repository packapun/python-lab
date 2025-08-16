# Python Lab

A collection of Python programming experiments, algorithm implementations, and coding practice solutions.

## Overview

This repository contains various Python implementations including:
- **Data Structures**: Binary search trees, linked lists, stacks, queues, heaps
- **Algorithms**: Sorting algorithms, pattern matching, string manipulation
- **LeetCode Solutions**: Common coding interview problems and solutions
- **Practice Problems**: Various algorithmic challenges and implementations
TODO add interview experiences and mocks.
TODO create a boss rush mode
## Repository Structure

```
python-lab/
├── main.py                    # Two Sum implementation with tests
├── lc.py                      # LeetCode problem solutions
├── bst.py                     # Binary Search Tree implementation
├── linkedlist.py              # Linked List data structure
├── stack.py                   # Stack implementation
├── heap.py                    # Heap data structure
├── queue_circular_buffer.py   # Circular queue implementation
├── custom_queue.py            # Custom queue implementation
├── sorting.py                 # Sorting algorithms
├── patterns.py                # Pattern matching algorithms
├── merge_intervals.py         # Interval merging problems
├── islands.py                 # Island counting algorithms
├── anagram_checker.py         # Anagram detection algorithms
└── practice/                  # Additional practice problems
    ├── two_sum.py
    ├── valid_brackets.py
    ├── k_most_frequent.py
    ├── longestsubset.py
    ├── longestzeroes.py
    └── playground.py
```

## Key Implementations

### Data Structures
- **Binary Search Tree** (`bst.py`): Complete BST with insertion, deletion, and traversal
- **Linked List** (`linkedlist.py`): Singly linked list with append and display methods
- **Stack** (`stack.py`): Stack implementation with push/pop operations
- **Heap** (`heap.py`): Min/max heap implementation
- **Queue** (`custom_queue.py`, `queue_circular_buffer.py`): Various queue implementations
- TODO: Add Fenwick tree

### Algorithms
- **Two Sum** (`main.py`): Multiple approaches to the classic two sum problem
- **Valid Parentheses** (`lc.py`): Bracket validation using stack
- **Anagram Detection** (`lc.py`): String anagram checking algorithms
- **Longest Substring** (`lc.py`): Finding longest substring without repeating characters
- **Top K Frequent** (`lc.py`): Finding k most frequent elements using heap
- **String Compression** (`lc.py`): In-place string compression algorithm
- **Longest Consecutive Sequence** (`lc.py`): Finding longest consecutive number sequence

## Usage

Each file can be run independently:

```bash
# Run main two sum implementation
python main.py

# Test specific algorithm implementations
python lc.py

# Test data structure implementations
python linkedlist.py
python bst.py
```

## Practice Problems

The `practice/` directory contains additional coding challenges and experimental implementations for skill development and interview preparation.

## License

This project is licensed under the terms specified in the LICENSE file.
