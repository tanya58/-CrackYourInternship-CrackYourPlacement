class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefix_s = 0
        res = 0
        prefix_cnt = defaultdict(int)
        prefix_cnt[0] = 1
        
        for n in nums:
            prefix_s += n
            remain = prefix_s % k
            
            if remain in prefix_cnt:
                res += prefix_cnt[remain]
            prefix_cnt[remain] += 1    
        return res        
        