class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        prefixes = []
        initialVal = 1
        for num in nums:
            prefixes.append(initialVal)
            initialVal *= num
        
        suffixes = [0] * len(nums)
        initialVal = 1
        for i in range(len(nums) - 1, -1, -1):
            suffixes[i] = initialVal
            initialVal *= nums[i]
        returnVal = []
        for i in range(len(nums)):
            returnVal.append(prefixes[i] * suffixes[i])
        return returnVal
        