class Solution:
    def numberOfAlternatingGroups(self, colors: List[int]) -> int:
        ans = 0
        n = len(colors)
        for i in range(0,n):
            if(colors[(i+1)%n] != colors[i] and colors[i] != colors[(i-1+n)%n]):
                ans += 1
                
        return ans        
        