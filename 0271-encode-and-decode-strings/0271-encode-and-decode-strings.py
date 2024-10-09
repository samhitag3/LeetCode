class Codec:

    def encode(self, strs):
        """Encodes a list of strings to a single string.
        
        :type strs: List[str]
        :rtype: str
        """
        returnVal = ""
        for s in strs:
            for c in s:
                o = ord(c)
                if o < 10:
                    returnVal += "00"
                elif o < 100:
                    returnVal += "0"
                returnVal += str(o)
            returnVal += "256"
        return returnVal
        

    def decode(self, s):
        """Decodes a single string to a list of strings.
        
        :type s: str
        :rtype: List[str]
        """
        returnVal = []
        i = 0
        while i < len(s):
            current = ""
            while s[i: i + 3] != "256":
                current += (chr(int(s[i: i + 3])))
                i += 3
            returnVal.append(current)
            i += 3
        return returnVal
            
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))