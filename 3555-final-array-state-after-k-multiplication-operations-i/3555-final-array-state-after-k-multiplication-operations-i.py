class Solution(object):
    def getFinalState(self, nums, k, multiplier):
        """
        :type nums: List[int]
        :type k: int
        :type multiplier: int
        :rtype: List[int]
        """
        for i in range(k):
            minIndex = nums.index(min(nums))
            nums[minIndex] = nums[minIndex] * multiplier
        return nums
        