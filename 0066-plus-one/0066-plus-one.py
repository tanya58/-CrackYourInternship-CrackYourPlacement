class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s = int(''.join([str(i) for i in digits]))
        s += 1
        result = list(str(s))
        return [int(i) for i in result]
        