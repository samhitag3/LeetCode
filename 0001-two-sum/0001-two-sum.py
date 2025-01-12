class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashMap = {}
        for i in range(len(nums)):
            if target - nums[i] in hashMap:
                return [i, hashMap[target - nums[i]]]
            else:
                hashMap[nums[i]] = i
        return []


        