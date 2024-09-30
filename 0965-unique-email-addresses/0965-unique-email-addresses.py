class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        actualEmails = []
        for e in emails:
            if "." in e:
                atInd = e.index("@")
                perInd = e.index(".")
                while perInd < atInd:
                    e = e[:perInd] + e[perInd + 1:]
                    atInd = e.index("@")
                    perInd = e.index(".")
            if "+" in e:
                plusInd = e.index("+")
                e = e[:plusInd] + e[atInd:]
            if e not in actualEmails:
                actualEmails.append(e)
        return len(actualEmails)
        