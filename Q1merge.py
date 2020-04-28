class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals = sorted(intervals, key = lambda x : x[0])
        print intervals
        i = 0
        res = []
        for interval in intervals:
            if res and (res[-1][1] >= interval[0] or res[-1][0] == interval[0]):
                res[-1][1] = max(res[-1][1], interval[1])
            else:
                res.append(interval)
        return res


intervals = [[1,3],[2,6],[8,10],[15,18]]
sol = Solution()
print sol.merge(intervals)