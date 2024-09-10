class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        for i in range(0, len(grid)):
            grid[i].sort()
        n = len(grid[0])
        res = 0
        for j in range(0, n):
            ans = 0
            for i in range(0, len(grid)):
                ans = max(ans, grid[i].pop())
            res += ans
            
        return res
        