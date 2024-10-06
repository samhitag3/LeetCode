class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        rows = len(matrix)
        cols = len(matrix[0])
        visited = []
        visits = 0
        for x in range(rows):
            visited.append([True] * cols)
        i = 0
        j = 0
        direction = "right"
        returnVal = []
        while visits < rows * cols:
            returnVal.append(matrix[i][j])
            visited[i][j] = False
            visits += 1
            if direction == "up":
                if i - 1 >= 0 and visited[i - 1][j]:
                    i -= 1
                else:
                    direction = "right"
                    j += 1
            elif direction == "right":
                if j + 1 < cols and visited[i][j + 1]:
                    j += 1
                else:
                    direction = "down"
                    i += 1
            elif direction == "down":
                if i + 1 < rows and visited[i + 1][j]:
                    i += 1
                else:
                    direction = "left"
                    j -= 1
            else:
                if j - 1 >= 0 and visited[i][j - 1]:
                    j -= 1
                else:
                    direction = "up"
                    i -= 1
        return returnVal


        