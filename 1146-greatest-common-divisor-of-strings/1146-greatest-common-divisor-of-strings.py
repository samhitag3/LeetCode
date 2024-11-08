class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        i = min(len(str1), len(str2))
        while i > 0:
            x = len(str1) // i
            y = len(str2) // i
            if x * str1[:i] == str1 and y * str1[:i] == str2:
                break
            else:
                i -= 1
        return str1[:i]