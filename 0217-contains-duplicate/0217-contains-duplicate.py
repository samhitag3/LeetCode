class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        # """
        numsSet = set()
        for n in nums:
            if n in numsSet:
                return True
            else:
                numsSet.add(n)
        return False

        # nums.sort()
        # for i in range(len(nums) - 1):
        #     if nums[i] == nums[i + 1]:
        #         return True
        # return False
        