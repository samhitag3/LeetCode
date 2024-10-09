class Solution(object):
    def minAddToMakeValid(self, s):
        """
        :type s: str
        :rtype: int
        """
        openP = 0
        extras = 0
        for c in s:
            if c == "(":
                openP += 1
            if c == ")":
                if openP > 0: openP -= 1
                else: extras += 1
        return extras + openP
        