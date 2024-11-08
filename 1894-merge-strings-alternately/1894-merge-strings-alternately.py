class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        i, j = 0, 0
        returnVal = ""
        while i < len(word1) or j < len(word2):
            if i == len(word1):
                returnVal += word2[j]
                j += 1
            elif j == len(word2):
                returnVal += word1[i]
                i += 1
            else:
                returnVal += word1[i]
                returnVal += word2[j]
                i += 1
                j += 1
        return returnVal