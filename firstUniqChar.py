class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        hash = {}

        for i in range(len(s)):
            hash[s[i]] = hash.get(s[i],0) + 1
        print hash


        for i in range(len(s)):
            if hash[s[i]]==1:
                return i
        return -1