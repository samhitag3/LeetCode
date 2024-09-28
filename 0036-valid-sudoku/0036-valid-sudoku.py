class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        current = []
        # boxes
        ranges = [[0, 3], [3, 6], [6, 9]]
        for x in ranges:
            for y in ranges:
                current = []
                for i in range(x[0], x[1]):
                    for j in range(y[0], y[1]):
                        if board[i][j] != '.':
                            if board[i][j] in current:
                                return False
                            else:
                                current.append(board[i][j])
        # rows
        for r in board:
            current = []
            for i in range(9):
                if r[i] != '.':
                    if r[i] in current:
                        return False
                    else:
                        current.append(r[i])
        # columns
        for j in range(9):
            current = []
            for i in range(9):
                if board[i][j] != '.':
                    if board[i][j] in current:
                        return False
                    else:
                        current.append(board[i][j])
        return True
        