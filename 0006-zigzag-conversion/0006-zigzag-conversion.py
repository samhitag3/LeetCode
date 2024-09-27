class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        elif numRows == 2:
            rows = ["", ""]
            for i in range(len(s)):
                if i % 2 == 0:
                    rows[0] += s[i]
                else:
                    rows[1] += s[i]
            return rows[0] + rows[1]

        rows = [""] * numRows
        r = 0
        down = True
        i = 0
        while i < len(s):
            if r == 0:
                while r < numRows and i < len(s):
                    rows[r] += s[i]
                    i += 1
                    r += 1
                r = numRows - 2
            else:
                rows[r] += s[i]
                # for j in range(numRows):
                #     if j == r:
                #         continue
                #     else:
                #         rows[j] += " "
                r -= 1
                i += 1
        returnVal = ""
        for h in rows:
            returnVal += h
        return returnVal
                


        