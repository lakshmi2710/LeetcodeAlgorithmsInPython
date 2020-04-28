class Solution(object):
    def countSubstrings(self, s):
        n = len(s)
        if n == 0:
            return 0

        res = [[False for i in range(n)] for j in range(n)]

        count = 0

        for i in range(n):
            res[i][i] = True
            count += 1

        for i in range(n - 1):
            if s[i] == s[i + 1]:
                res[i][i + 1] = True
                count += 1

        for k in range(3, n + 1):
            for i in range(n - k + 1):
                j = i + k - 1
                if res[i + 1][j - 1] and s[i] == s[j]:
                    res[i][j] = True
                    count += 1

        return count
