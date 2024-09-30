class Solution(object):
    def licenseKeyFormatting(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        # print(ord('a'), ord('z')) - 97-122
        # print(ord('A'), ord('Z')) - 65-90
        # print(ord('0'), ord('9')) - 48-57
        justKey = ""
        for c in s:
            o = ord(c)
            if o >= 97 and o <= 122:
                justKey += chr(o - 32)
            elif o >= 65 and o <= 90:
                justKey += c
            elif o >= 48 and o <= 57:
                justKey += c
        groups = int(len(justKey) / k)
        smallGroup = len(justKey) % k
        returnVal = justKey[:smallGroup]
        if smallGroup != 0:
            for i in range(groups):
                returnVal += "-"
                returnVal += justKey[smallGroup + i*k:smallGroup + (i + 1)*k]
        else:
            for i in range(groups):
                returnVal += justKey[i*k:(i + 1)*k]
                returnVal += "-"
            returnVal = returnVal[:len(returnVal) - 1]
        return returnVal

        