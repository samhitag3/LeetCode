from collections import Counter
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        wordDicts = []
        returnVal = []
        for s in strs:
            d = Counter(s)
            if d in wordDicts:
                i = wordDicts.index(d)
                returnVal[i].append(s)
            else:
                wordDicts.append(d)
                returnVal.append([s])
        return returnVal
        