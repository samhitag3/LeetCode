class Solution(object):
    def rankTeams(self, votes):
        """
        :type votes: List[str]
        :rtype: str
        """
        teams = []
        for i in range(26):
            teams.append([0] * 26 + [-i])
        for v in votes:
            for i in range(len(v)):
                teams[ord(v[i]) - 65][i] += 1
        teams.sort(reverse=True)
        returnVal = ""
        for i in range(26):
            c = chr((-1) * (teams[i][26]) + 65)
            if c in votes[0]:
                returnVal += c
        return returnVal




        