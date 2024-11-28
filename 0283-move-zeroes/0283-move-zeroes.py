class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        zeroes = []
        for i in range(len(nums)):
            if nums[i] == 0:
                zeroes.append(i)
        i = 0
        for i in range(len(zeroes)):
            nums.pop(zeroes[i] - i)
            nums.append(0)

        