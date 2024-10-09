class Solution(object):
    def minSetSize(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        arrDict = {}
        for a in arr:
            if a in arrDict:
                arrDict[a] += 1
            else:
                arrDict[a] = 1
        l = (len(arr) / 2)
        arr = list(arrDict)
        arr.sort(reverse=True, key=lambda x: arrDict[x])
        removals = 0
        count = 0
        i = 0
        while removals < l:
            removals += arrDict[arr[i]]
            count += 1
            i += 1
        return count