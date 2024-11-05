class Solution(object):
    def areaOfMaxDiagonal(self, dimensions):
        """
        :type dimensions: List[List[int]]
        :rtype: int
        """
        dimensions.sort(reverse=True, key=lambda x: x[0] * x[1])
        diagonals = [((d[0] ** 2 + d[1] ** 2) ** 0.5) for d in dimensions]
        i = diagonals.index(max(diagonals))
        return dimensions[i][0] * dimensions[i][1]