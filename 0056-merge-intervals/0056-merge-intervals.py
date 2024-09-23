class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) < 2:
            return intervals
        
        intervals = sorted(intervals, key = lambda x: (x[0], x[1]))

        result = [intervals[0]]
        c = 0
        for x in intervals[1:]:
            if result[c][1] >= x[0]:
                if result[c][1] < x[1]:
                    result[c][1] = x[1]
            else:
                result.append(x)
                c += 1
        
        return result
        