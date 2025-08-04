from collections import deque
from typing import List

def orangesRotting(self, grid: List[List[int]]) -> int:
    if not grid or not grid[0]:
        return 0
    
    queue = deque()
    m, n = len(grid), len(grid[0])
    fresh_count = 0
    
    # Find all initially rotten oranges and count fresh ones
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 2:
                queue.append((i, j))
            elif grid[i][j] == 1:
                fresh_count += 1
    
    # If no fresh oranges, no time needed
    if fresh_count == 0:
        return 0
    
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    time_elapsed = 0
    
    while queue:
        # Process all oranges at current time level
        level_size = len(queue)
        newly_rotten = 0
        
        for _ in range(level_size):
            row, col = queue.popleft()
            
            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc
                
                if (0 <= new_row < m and 0 <= new_col < n and 
                    grid[new_row][new_col] == 1):
                    # Mark as rotten and add to queue
                    grid[new_row][new_col] = 2
                    queue.append((new_row, new_col))
                    newly_rotten += 1
        
        # Only increment time if we actually rotted some oranges
        if newly_rotten > 0:
            time_elapsed += 1
            fresh_count -= newly_rotten
    
    # Return -1 if any fresh oranges remain, otherwise return time
    return -1 if fresh_count > 0 else time_elapsed