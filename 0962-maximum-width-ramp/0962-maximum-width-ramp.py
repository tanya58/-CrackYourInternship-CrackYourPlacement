class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        stack = []
        n = len(nums)
        # Stack Formation
        for i in range(n):
            if not stack or nums[i] < nums[stack[-1]]:
                stack.append(i)
        max_width = 0
        # Traverse the array backwards
        for j in range(n-1, -1, -1):
            while stack and nums[j] >= nums[stack[-1]]:
                max_width = max(max_width, j - stack.pop())
        return max_width
        