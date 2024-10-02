class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        wordDicts = []
        returnVal = []
        for s in strs:
            currentDict = {}
            for c in s:
                if c in currentDict:
                    currentDict[c] += 1
                else:
                    currentDict[c] = 1
            if currentDict in wordDicts:
                returnVal[wordDicts.index(currentDict)].append(s)
            else:
                wordDicts.append(currentDict)
                returnVal.append([s])
        return returnVal
        