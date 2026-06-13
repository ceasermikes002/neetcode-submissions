class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Check to ensure both strings aren't of equal length
        if len(s) != len(t):
            return False

        # Initialize our Hashmap
        countS, countT = {}, {}

        # Build our hashmap
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        for c in countS:
            if countS[c] != countT.get(c, 0):
                return False
        return True
        