class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return len(nums)
        count = 0
        i = 0
        while i < len(nums) - 1 and nums[i] != '_':
            if nums[i] == nums[i + 1]:
                nums.pop(i + 1)
                nums.append('_')
                count += 1
            else:
                i += 1
        return len(nums) - count
        