class DAG(object):
    def __init__(self, n):
        self.n = n
        self.E = []
        for i in range(n):
            self.E.append([0] * self.n)
    
    def addEdge(self, x, y):
        self.E[x][y] = 1
    
    def longestPath(self):
        L = [0] * self.n
        for j in range(self.n):
            maxL = 0
            for i in range(self.n):
                if self.E[i][j]:
                    if L[i] > maxL:
                        maxL = L[i]
            L[j] = maxL + 1
        return max(L)
    
    def printDAG(self):
        for v in self.E:
            print(v)
        
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dag = DAG(len(nums))
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    dag.addEdge(i, j)
        return dag.longestPath()
