class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        while "()" in s or "{}" in s or "[]" in s:
            if "()" in s:
                i = s.index("()")
                s = s[:i] + s[i+2:]
            if "{}" in s:
                i = s.index("{}")
                s = s[:i] + s[i+2:]
            if "[]" in s:
                i = s.index("[]")
                s = s[:i] + s[i+2:]
        return len(s) == 0

        