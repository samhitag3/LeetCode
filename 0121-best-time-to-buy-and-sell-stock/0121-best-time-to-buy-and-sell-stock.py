class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        lowVals = []
        l = len(prices)
        val = prices[0]
        for i in range(l):
            if prices[i] < val:
                val = prices[i]
            lowVals.append(val)
        print(lowVals)
        highVals = [0] * l
        val = prices[l - 1]
        for i in range(l - 1, -1, -1):
            if prices[i] > val:
                val = prices[i]
            highVals[i] = val
        print(highVals)
        val = 0
        for i in range(l):
            diff = highVals[i] - lowVals[i]
            if diff > val:
                val = diff
        return val


        
        