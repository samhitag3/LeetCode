class Solution(object):
    def maximumSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        currDict = {}
        currSum = 0
        for i in range(k):
            if nums[i] in currDict:
                currDict[nums[i]] += 1
            else:
                currDict[nums[i]] = 1
            currSum += nums[i]
        currRepeats = set()
        for key in currDict:
            if currDict[key] > 1:
                currRepeats.add(key)
        currMax = 0
        if len(currRepeats) == 0:
            currMax = currSum
        i = 0
        while i < (len(nums) - (k - 1)):

            if len(currRepeats) == 0 and currSum > currMax:
                currMax = currSum
    
            currDict[nums[i]] -= 1
            if currDict[nums[i]] == 1:
                currRepeats.remove(nums[i])
            if i + k < len(nums):
                if nums[i + k] in currDict:
                    currDict[nums[i + k]] += 1
                    if currDict[nums[i + k]] == 2:
                        currRepeats.add(nums[i + k])
                else:
                    currDict[nums[i + k]] = 1

                currSum -= nums[i]
                currSum += nums[i + k]

            i += 1
        return currMax


            


    
        