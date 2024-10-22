class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        # if len(s3) != len(s1) + len(s2):  # Check if lengths match
        #     return False

        matrix = []
        for i in range(len(s1) + 1):
            matrix.append([-1] * (len(s2) + 1))

        def check(i, j, val):
            if matrix[i][j] > -1:
                return matrix[i][j]
            elif len(val) != (i + j):
                matrix[i][j] = 0
            elif len(val) == 0:
                matrix[i][j] = 1
            elif i == 0:
                matrix[i][j] = int(s2[:j] == val)
            elif j == 0:
                matrix[i][j] = int(s1[:i] == val)
            else:
                matrix[i][j] = 0  # Default to false unless proven true
                if s1[i - 1] == val[len(val) - 1]:
                    matrix[i][j] |= check(i - 1, j, val[:len(val) - 1])  # Check from s1
                if s2[j - 1] == val[len(val) - 1]:
                    matrix[i][j] |= check(i, j - 1, val[:len(val) - 1])  # Check from s2
            return matrix[i][j]

        x = bool(check(len(s1), len(s2), s3))
        return x
