class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        goodOranges = []
        rottenOranges = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    goodOranges.append([i, j])
                elif grid[i][j] == 2:
                    rottenOranges.append([i, j])
        minute = 0
        print(goodOranges)
        print(rottenOranges)
        while len(goodOranges) > 0:
            newRots = []
            for o in rottenOranges:
                if [o[0], o[1] + 1] in goodOranges:
                    goodOranges.remove([o[0], o[1] + 1])
                    newRots.append([o[0], o[1] + 1])
                if [o[0] + 1, o[1]] in goodOranges:
                    goodOranges.remove([o[0] + 1, o[1]])
                    newRots.append([o[0] + 1, o[1]])
                if [o[0], o[1] - 1] in goodOranges:
                    goodOranges.remove([o[0], o[1] - 1])
                    newRots.append([o[0], o[1] - 1])
                if [o[0] - 1, o[1]] in goodOranges:
                    goodOranges.remove([o[0] - 1, o[1]])
                    newRots.append([o[0] - 1, o[1]])
            if len(newRots) == 0:
                return -1
            rottenOranges.extend(newRots)
            minute += 1
        return minute

        