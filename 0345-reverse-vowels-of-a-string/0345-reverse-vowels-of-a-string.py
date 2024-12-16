class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        vowelIndices = []
        for i in range(len(s)):
            if s[i] in vowels:
                vowelIndices.append(i)
        for i in range(len(vowelIndices) // 2):
            s = s[:vowelIndices[i]] + s[vowelIndices[len(vowelIndices) - 1 - i]] + s[vowelIndices[i] + 1:vowelIndices[len(vowelIndices) - 1 - i]] + s[vowelIndices[i]] + s[vowelIndices[len(vowelIndices) - 1 - i] + 1:]
        return s

        