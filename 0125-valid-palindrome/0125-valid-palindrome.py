class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # 48-57 - 0-9
        # 65-90 - uppercase
        # 97-122 - lowercase
        strRep = []
        for x in s:
            o = ord(x)
            if (o >= 48 and o <= 57) or (o >= 65 and o <= 90) or (o >= 97 and o <= 122):
                if (o >= 97 and o <= 122):
                    strRep.append(chr(o - 32))
                else:
                    strRep.append(x)
        while len(strRep) > 1:
            if strRep.pop(0) != strRep.pop():
                return False
        return True
