from collections import Counter
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = len(Counter(s).values())
        for x in range(l, 0, -1):
            for i in range(0, len(s) - x + 1):
                if sorted(list(Counter(s[i:i+x]).values()), reverse=True)[0] == 1:
                    return x
        return 0

        