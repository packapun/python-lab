class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None

class Solution:
    def findWords(self, board, words):
        """
        Find all words from the word list that can be constructed on the board.
        
        Args:
            board: List[List[str]] - m x n board of characters
            words: List[str] - list of words to search for
            
        Returns:
            List[str] - words found on the board
        """
        # Build Trie from words
        root = self.buildTrie(words)
        
        # Result list
        result = []
        
        # Search each cell as starting point
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                self.dfs(board, i, j, root, result)
        
        return result
    
    def buildTrie(self, words):
        """Build a Trie from the list of words."""
        root = TrieNode()
        for word in words:
            node = root
            for char in word:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
            node.word = word  # Store the complete word at the end node
        return root
    
    def dfs(self, board, i, j, node, result):
        """
        Depth-first search to find words starting from position (i, j).
        
        Args:
            board: the game board
            i, j: current position
            node: current TrieNode
            result: list to store found words
        """
        # Get current character
        char = board[i][j]
        
        # Check if current character exists in Trie
        if char not in node.children:
            return
        
        # Move to next node in Trie
        node = node.children[char]
        
        # Check if we found a complete word
        if node.word:
            result.append(node.word)
            node.word = None  # Avoid duplicate results
        
        # Mark current cell as visited
        board[i][j] = '#'
        
        # Explore all 4 directions
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for di, dj in directions:
            ni, nj = i + di, j + dj
            # Check bounds and if cell is not visited
            if (0 <= ni < len(board) and 
                0 <= nj < len(board[0]) and 
                board[ni][nj] != '#'):
                self.dfs(board, ni, nj, node, result)
        
        # Backtrack: restore the original character
        board[i][j] = char

# Test the solution
def test_solution():
    solution = Solution()
    
    # Test case 1
    board1 = [
        ["o","a","a","n"],
        ["e","t","a","e"],
        ["i","h","k","r"],
        ["i","f","l","v"]
    ]
    words1 = ["oath","pea","eat","rain"]
    result1 = solution.findWords(board1, words1)
    print(f"Test 1 - Expected: ['eat','oath'], Got: {result1}")
    
    # Test case 2
    board2 = [
        ["a","b"],
        ["c","d"]
    ]
    words2 = ["abcb"]
    result2 = solution.findWords(board2, words2)
    print(f"Test 2 - Expected: [], Got: {result2}")
    
    # Additional test case
    board3 = [
        ["a","b","c"],
        ["a","e","d"],
        ["a","f","g"]
    ]
    words3 = ["abcdefg", "gfedcba", "eaabcdgfa", "befa", "ae", "ea"]
    result3 = solution.findWords(board3, words3)
    print(f"Test 3 - Result: {result3}")

if __name__ == "__main__":
    test_solution()
