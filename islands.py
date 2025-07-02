
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        Count number of islands in a 2D grid.
        An island is formed by connecting adjacent lands horizontally or vertically.
        
        Time: O(m*n), Space: O(min(m,n)) for recursion stack
        """
        if not grid or not grid[0]:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        islands = 0
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                    self._sink_island(grid, i, j)
                    islands += 1
        
        return islands
    
    def _sink_island(self, grid: List[List[str]], row: int, col: int) -> None:
        """Sink all connected land using DFS."""
        # Boundary check and water check
        if (row < 0 or row >= len(grid) or 
            col < 0 or col >= len(grid[0]) or 
            grid[row][col] != '1'):
            return
        
        # Sink this land
        grid[row][col] = '0'
        
        # Explore all 4 directions
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for dr, dc in directions:
            self._sink_island(grid, row + dr, col + dc)
