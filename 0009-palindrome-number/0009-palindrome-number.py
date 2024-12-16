class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        xStr = str(x)
        def helper(s):
            if len(s) < 2:
                return True
            elif s[0] != s[len(s) - 1]:
                return False
            return helper(s[1:len(s) - 1])
        return helper(xStr)
