# The audio-analysis team presents a snippet of music in the form of a 2D pitch sheet. 
# They're looking to find the longest accending sequence through all the noise. 
# Each cell holds a pitch (0 – 127). A melody path is a sequence of cells that:

# * starts at any cell;
# * moves orthogonally (up, down, left, right) one step at a time;
# * never visits the same cell twice;
# * is strictly increasing in pitch (every next note has a higher value)

# 27 30 60 50
# 30 31 64 70 
# 28 23 65 66

from typing import List

def findLongestSequence(matrix: List[List[int]]):
    if not matrix or not matrix[0]:
        return 0
    
    m, n = len(matrix), len(matrix[0])
    max_length = 0
    
    for i in range(m):
        for j in range(n):
            # Start DFS from each cell with length 1 (the starting cell itself)
            curr_length = dfs(matrix, i, j, 1)
            max_length = max(curr_length, max_length)
    
    return max_length

def dfs(matrix, i, j, length):
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    curr_value = matrix[i][j]
    max_length = length
    
    # Mark current cell as visited
    matrix[i][j] = -1
    
    for di, dj in directions:
        ni, nj = i + di, j + dj
        # Check bounds and if next cell has higher value than current
        if (0 <= ni < len(matrix) and 0 <= nj < len(matrix[0]) and 
            matrix[ni][nj] >= 0 and curr_value < matrix[ni][nj]):
            
            max_length = max(dfs(matrix, ni, nj, length + 1), max_length)
    
    # Restore current cell value (backtrack)
    matrix[i][j] = curr_value
    return max_length

# Alternative version that also tracks the actual sequence
def findLongestSequenceWithPath(matrix: List[List[int]]):
    if not matrix or not matrix[0]:
        return 0, []
    
    m, n = len(matrix), len(matrix[0])
    max_length = 0
    best_sequence = []
    
    for i in range(m):
        for j in range(n):
            sequence = []
            curr_length = dfs_with_path(matrix, i, j, 1, sequence)
            if curr_length > max_length:
                max_length = curr_length
                best_sequence = sequence.copy()
    
    return max_length, best_sequence

def dfs_with_path(matrix, i, j, length, sequence):
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    curr_value = matrix[i][j]
    max_length = length
    best_sequence = []
    
    # Add current value to sequence
    sequence.append(curr_value)
    
    # Mark current cell as visited
    matrix[i][j] = -1
    
    for di, dj in directions:
        ni, nj = i + di, j + dj
        # Check bounds and if next cell has higher value than current
        if (0 <= ni < len(matrix) and 0 <= nj < len(matrix[0]) and 
            matrix[ni][nj] >= 0 and curr_value < matrix[ni][nj]):
            
            temp_length = dfs_with_path(matrix, ni, nj, length + 1, sequence)
            if temp_length > max_length:
                max_length = temp_length
                best_sequence = sequence.copy()
    
    # Restore current cell value (backtrack)
    matrix[i][j] = curr_value
    sequence.pop()  # Remove current value from sequence
    
    # Update the original sequence with the best found
    if best_sequence:
        sequence.extend(best_sequence[len(sequence):])
    
    return max_length

# Test the solution
matrix = [[27, 30, 60, 50], [30, 31, 64, 70], [28, 23, 65, 66]]

print("Matrix:")
for row in matrix:
    print(row)

print(f"\nLongest ascending sequence length: {findLongestSequence(matrix)}")

# Test with path tracking
matrix2 = [[27, 30, 60, 50], [30, 31, 64, 70], [28, 23, 65, 66]]
length, path = findLongestSequenceWithPath(matrix2)
print(f"Longest sequence length: {length}")
print(f"Sequence: {path}")

# Additional test cases
print("\n--- Additional Test Cases ---")

# Test case 2: Simple increasing
matrix3 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(f"Test 2 result: {findLongestSequence(matrix3)}")

# Test case 3: All same values (should return 1)
matrix4 = [[5, 5, 5], [5, 5, 5]]
print(f"Test 3 result: {findLongestSequence(matrix4)}")

# Test case 4: Single cell
matrix5 = [[42]]
print(f"Test 4 result: {findLongestSequence(matrix5)}")

"""
The algorithm has a time complexity of O(4^(m×n)) in the worst case, where m and n are the matrix dimensions, since each cell can potentially explore 4 directions recursively.
"""



