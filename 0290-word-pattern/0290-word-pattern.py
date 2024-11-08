class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        words = s.split(' ')
        if len(pattern) != len(words):
            return False
        function = {}
        rangeF = set()
        for i in range(len(pattern)):
            if pattern[i] in function:
                if function[pattern[i]] != words[i]:
                    return False
            else:
                function[pattern[i]] = words[i]
                rangeF.add(words[i])
        return len(function) == len(rangeF)
                    
        