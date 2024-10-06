class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if len(nums) == 0:
            return []
        if len(nums) == 1:
            return[str(nums[0])]
        a = nums[0]
        b = nums[0]
        returnVal = []
        for i in range(1, len(nums)):
            if nums[i] != b + 1:
                if a == b:
                    returnVal.append(str(a))
                else:
                    apppy = str(a)
                    apppy += "->"
                    apppy += str(b)
                    returnVal.append(apppy)
                a = nums[i]
                b = nums[i]
            else:
                b += 1
        if a == b:
            returnVal.append(str(a))
        else:
            apppy = str(a)
            apppy += "->"
            apppy += str(b)
            returnVal.append(apppy)
        return returnVal

        