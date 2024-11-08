class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        results = []
        def process(x):
            total = 0
            while x > 0:
                total += (x % 10) ** 2
                x //= 10
            return total
        results.append(n)
        i = n
        while True:
            i = process(i)
            if i == 1:
                return True
            elif i in results:
                return False
            else:
                results.append(i)