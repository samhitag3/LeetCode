class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        # chars.insert(1, "e")
        # chars.remove()
        i = 0
        while i < len(chars):
            c = chars[i]
            i += 1
            if i < len(chars) and c == chars[i]:
                count = 1
                while i < len(chars) and c == chars[i]:
                    del chars[i]
                    count += 1
                word = str(count)
                for w in word:
                    chars.insert(i, w)
                    i += 1
        return len(chars)

            

            
            
        
            