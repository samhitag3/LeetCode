class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        bijection = {}
        fRange = set()
        for i in range(len(s)):
            if s[i] in bijection:
                if bijection[s[i]] != t[i]:
                    return False
            else:
                if t[i] in fRange:
                    return False
                else:
                    bijection[s[i]] = t[i]
                    fRange.add(t[i])
        return True
        