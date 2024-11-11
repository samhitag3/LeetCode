from collections import Counter
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        rnDict = Counter(ransomNote)
        mDict = Counter(magazine)
        for k in rnDict:
            if k in mDict:
                if rnDict[k] > mDict[k]:
                    return False
            else:
                return False
        return True
        