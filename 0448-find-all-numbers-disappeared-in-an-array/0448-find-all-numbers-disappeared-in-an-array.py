class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for n in nums:
            i=abs(n)-1
            nums[i] = -1 * abs(nums[i])
        
        # returning non marked num in nums
        res=[] # in question they mentioned :- You may assume the returned list does not count as extra space.
        for i,n in enumerate(nums):
            if n>0:
                res.append(i+1)

        return res
        