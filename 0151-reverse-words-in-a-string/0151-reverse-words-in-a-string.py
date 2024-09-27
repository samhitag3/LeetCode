class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        words = s.split()
        newSentence = words[len(words) - 1]
        for i in range(len(words) - 2, -1, -1):
            newSentence += " "
            newSentence += words[i]
        return newSentence
        