class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 2: return n
    
        x = [0] * (n + 1)
        x[1] = 1
        for i in range(2, n + 1):
            x[i] = x[i - 1] + x[i - 2]
        return x[n]
        