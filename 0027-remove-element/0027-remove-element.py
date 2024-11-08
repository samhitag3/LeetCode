class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        count = 0
        while val in nums:
            nums.remove(val)
            nums.append('_')
            count += 1
        return len(nums) - count

        