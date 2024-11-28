class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m = max(nums)
        for i in range(m):
            if i not in nums:
                return i
        return m + 1
        