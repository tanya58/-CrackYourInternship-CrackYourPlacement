class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        N = len(nums)
        target = nums[N//2]
        
        return sum(abs(target - n)for n in nums)
        