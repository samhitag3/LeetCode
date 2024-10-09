class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        sDict = {}
        tDict = {}
        for c in s:
            if c in sDict:
                sDict[c] += 1
            else:
                sDict[c] = 1
        for c in t:
            if c in tDict:
                tDict[c] += 1
            else:
                tDict[c] = 1
        return sDict == tDict
        