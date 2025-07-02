class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        Merge overlapping intervals.
        
        Time: O(n log n) for sorting, Space: O(1) excluding output
        """
        if not intervals:
            return []
        
        # Sort by start time
        intervals.sort(key=lambda x: x[0])
        
        merged = [intervals[0]]
        
        for current in intervals[1:]:
            last_merged = merged[-1]
            
            # If current interval overlaps with last merged interval
            if current[0] <= last_merged[1]:
                # Extend the last merged interval
                last_merged[1] = max(last_merged[1], current[1])
            else:
                # No overlap, add current interval
                merged.append(current)
        
        return merged
