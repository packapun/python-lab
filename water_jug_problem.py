class Solution:
    def canMeasureWater(self, jugOneCapacity: int, jugTwoCapacity: int, targetCapacity: int) -> bool:
        """
        Determine if we can measure exactly targetCapacity liters using two jugs.
        
        Time Complexity: O(log(min(a, b))) where a and b are the jug capacities
        Space Complexity: O(1)
        """
        # Edge cases
        if targetCapacity == 0:
            return True
        
        if targetCapacity > jugOneCapacity + jugTwoCapacity:
            return False
        
        # Helper function to calculate GCD using Euclidean algorithm
        def gcd(a: int, b: int) -> int:
            while b:
                a, b = b, a % b
            return a
        
        # The target is achievable if it's divisible by GCD of the two capacities
        return targetCapacity % gcd(jugOneCapacity, jugTwoCapacity) == 0


# Alternative BFS Solution (more intuitive but less efficient)
from collections import deque

class SolutionBFS:
    def canMeasureWater(self, jugOneCapacity: int, jugTwoCapacity: int, targetCapacity: int) -> bool:
        """
        BFS approach to explore all possible states.
        
        Time Complexity: O(x * y) where x and y are the jug capacities
        Space Complexity: O(x * y)
        """
        if targetCapacity == 0:
            return True
        
        if targetCapacity > jugOneCapacity + jugTwoCapacity:
            return False
        
        # State: (amount in jug1, amount in jug2)
        visited = set()
        queue = deque([(0, 0)])
        visited.add((0, 0))
        
        while queue:
            jug1, jug2 = queue.popleft()
            
            # Check if we've reached the target
            if jug1 == targetCapacity or jug2 == targetCapacity or jug1 + jug2 == targetCapacity:
                return True
            
            # All possible next states
            next_states = [
                (jugOneCapacity, jug2),  # Fill jug1
                (jug1, jugTwoCapacity),   # Fill jug2
                (0, jug2),                # Empty jug1
                (jug1, 0),                # Empty jug2
                # Pour jug1 -> jug2
                (max(0, jug1 - (jugTwoCapacity - jug2)), 
                 min(jugTwoCapacity, jug2 + jug1)),
                # Pour jug2 -> jug1
                (min(jugOneCapacity, jug1 + jug2),
                 max(0, jug2 - (jugOneCapacity - jug1)))
            ]
            
            for state in next_states:
                if state not in visited:
                    visited.add(state)
                    queue.append(state)
        
        return False


# Test cases
def test_solution():
    sol = Solution()
    
    # Test case 1: jug1=3, jug2=5, target=4
    assert sol.canMeasureWater(3, 5, 4) == True
    print("Test 1 passed: (3, 5, 4) -> True")
    
    # Test case 2: jug1=2, jug2=6, target=5
    assert sol.canMeasureWater(2, 6, 5) == False
    print("Test 2 passed: (2, 6, 5) -> False")
    
    # Test case 3: jug1=1, jug2=2, target=3
    assert sol.canMeasureWater(1, 2, 3) == True
    print("Test 3 passed: (1, 2, 3) -> True")
    
    # Test case 4: Edge case - target is 0
    assert sol.canMeasureWater(5, 3, 0) == True
    print("Test 4 passed: (5, 3, 0) -> True")
    
    # Test case 5: Target exceeds total capacity
    assert sol.canMeasureWater(2, 3, 10) == False
    print("Test 5 passed: (2, 3, 10) -> False")
    
    print("\nAll tests passed!")

if __name__ == "__main__":
    test_solution()