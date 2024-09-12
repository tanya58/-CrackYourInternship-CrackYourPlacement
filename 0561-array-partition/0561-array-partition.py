class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        sortedNums = sorted(nums)
        return sum([min((sortedNums[i], sortedNums[i+1])) for i in range(0, len(sortedNums)-1, 2)])
        