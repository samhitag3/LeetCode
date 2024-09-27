class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numsDict = {}
        for x in nums:
            if x in numsDict:
                numsDict[x] += 1
            else:
                numsDict[x] = 1
        amt = 0
        num = nums[0]
        for k in numsDict:
            if numsDict[k] > amt:
                amt = numsDict[k]
                num = k
        return num
        