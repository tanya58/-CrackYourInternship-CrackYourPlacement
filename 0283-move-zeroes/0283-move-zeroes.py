class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        size = len(nums)
        if(size == 0 or size == 1):
            return
        
        nz = 0
        z = 0
        while(nz < size):
            if(nums[nz] != 0):
                temp = nums[nz]
                nums[nz] = nums[z]
                nums[z] = temp
                nz += 1
                z += 1
            else:
                nz += 1
        