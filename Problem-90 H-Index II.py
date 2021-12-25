# 275. H-Index II
# https://leetcode.com/problems/h-index-ii/

# Time Complexity: O(log n)
# Space Complexity: O(1)

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        left = 0
        right = n - 1
        
        while left <= right:
            mid = left + (right-left)//2
            
            if citations[mid] == n - mid:
                return n - mid
            
            if citations[mid] < n - mid:
                left = mid + 1
            else:
                right = mid - 1
                    
        return n - left