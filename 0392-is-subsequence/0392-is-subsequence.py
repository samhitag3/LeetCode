class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        i = 0
        j = 0
        if len(s) == 0:
            return True
        while i < len(t):
            if t[i] == s[j]:
                j += 1
                if j == len(s):
                    return True
            i += 1
        return False

        