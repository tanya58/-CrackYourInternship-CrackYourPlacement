class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        numbers = sorted(nums)
        pro1 = numbers[-1] * numbers[-2] * numbers[-3]
        pro2 =  numbers[0] * numbers[1] * numbers[-1]
        return max(pro1, pro2)

        