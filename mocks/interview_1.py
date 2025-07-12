# The audio-analysis team presents a snippet of music in the form of a 2D pitch sheet. They're looking to find the longest accending sequence through all the noise. Each cell holds a pitch (0 – 127). A melody path is a sequence of cells that:

# * starts at any cell;
# * moves orthogonally (up, down, left, right) one step at a time;
# * never visits the same cell twice;
# * is strictly increasing in pitch (every next note has a higher value)

# 27 30 60 50
# 30 31 64 70 
# 28 23 65 66


# Test 

# def say_hello():
#     print('Hello, World')

# for i in range(5):
#     say_hello()


"""
Observations 
1. The input is a 2D matrix
2. The output is an integer which is the longest sequence 

Assumptions:
1. No null or empty values 
2. You can assume a sequence of length >= 1
3. Pitch goes from 0-127
4. You cannot move in diagnols
5. Equal values are not present in the sequences 


Simple Approach:
1. Start at a cell 
2. Kickstart DFS using this cell as a starting node 
3. Keep a counter variable to track the maximum depth
4. Only move in valid directions 
    4.1 up,down,left,right
    4.2 bounded by the edges of the matrix(within bounds)
    4.3 Only in ascending order (equal not allowed)
5. Update the max length based on sequence length 
6. Repeat 1-5 for all possible starting points
""" 

from typing import List 

def longestSequence(matrix:List[List[int]]) -> int:
    if not matrix or not matrix[0]:
        return 0

    max_sequence_size = 0 
    m = len(matrix)
    n = len(matrix[0])
    for i in range(0,len(matrix)):
        for j in range(0,len(matrix[0])):
            stack = []
            stack.append([i,j]) # 27
            current_max_sequence = 0
            current_max_sequence = dfs(matrix, i, j, m, n, stack, current_max_sequence)
            max_sequence_size = max(max_sequence_size, current_max_sequence)

    return max_sequence_size


def dfs(matrix, i, j, m, n, stack, current_max_sequence) -> int:
    valid_movements = [[-1,0],[1,0], [0,1], [0,-1]]
    start = stack.pop() # (0,0)
    curr_value = matrix[i][j] # 27
    
    for move in valid_movements:
        # Is within bounds [x]
        # Is increasing in value [x]
        # have we seen this index before 
        # Maintain a count
        next_index = [start[0] + move[0], start[1] + move[1]]
        if next_index[0] < m and next_index[1] < n and next_index not in stack:
            # 30, 30
            next_value = matrix[next_index[0], next_index[1]]
            if next_value > curr_value:
                current_max_sequence += 1
                stack.append(next_index)
                dfs(matrix, i,j,m,n,stack, current_max_sequence)
    return current_max_sequence



EXAMPLE = [
    [27, 30, 60, 50],
    [30, 31, 64, 70],
    [28, 23, 65, 66],
]
