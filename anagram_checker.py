from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Check if two strings are anagrams of each other.
        
        Algorithm: Compare character frequency counts of both strings.
        Runtime: O(len(s) + len(t))
        Space: O(max(len(s), len(t)))
        """
        return Counter(s) == Counter(t)

# Alternative approaches:

class SolutionAlternative1:
    def isAnagram(self, s: str, t: str) -> bool:
        """Using sorted strings - simple but less efficient for large strings."""
        return sorted(s) == sorted(t)

class SolutionAlternative2:
    def isAnagram(self, s: str, t: str) -> bool:
        """Using defaultdict - more explicit about the counting logic."""
        if len(s) != len(t):
            return False
        
        from collections import defaultdict
        count = defaultdict(int)
        
        for char in s:
            count[char] += 1
        
        for char in t:
            count[char] -= 1
            if count[char] == 0:
                del count[char]
        
        return not count

class SolutionAlternative3:
    def isAnagram(self, s: str, t: str) -> bool:
        """Manual counting with dict.get() - improvement over original."""
        if len(s) != len(t):
            return False
        
        count_map = {}
        
        # Count characters in s
        for char in s:
            count_map[char] = count_map.get(char, 0) + 1
        
        # Subtract characters in t
        for char in t:
            if char not in count_map:
                return False
            count_map[char] -= 1
            if count_map[char] == 0:
                del count_map[char]
        
        return not count_map