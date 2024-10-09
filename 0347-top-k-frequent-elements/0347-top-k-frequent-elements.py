class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        numsDict = {}
        for n in nums:
            if n in numsDict:
                numsDict[n] += 1
            else:
                numsDict[n] = 1
        nums = list(numsDict)
        nums.sort(reverse=True, key = lambda x: numsDict[x])
        return nums[:k]
        