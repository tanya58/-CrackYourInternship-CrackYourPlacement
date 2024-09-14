class Solution {
public:
    int jump(vector<int>& nums) {
         int left =0, right = 0;
        int levelMax = 0;
        int jump = 0;
        int n = nums.size();
        while(right < n-1){
            jump++;
            for(int i =left; i<=right; i++)
            {
                levelMax = max(levelMax, i+nums[i]);
            }
            left = right+1;
            right = levelMax;
        }

        // we came here when right >= n-1. This means that we reached the end in the last jump.
        return jump;
    }
};