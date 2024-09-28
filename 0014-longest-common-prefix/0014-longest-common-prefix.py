class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 1:
            return strs[0]
        i = 0
        while i < len(strs[0]):
            letter = strs[0][i]
            done = False
            for s in strs:
                if i >= len(s) or s[i] != letter:
                    done = True
                    break
            if done:
                break
            i += 1
        return strs[0][:i]
        