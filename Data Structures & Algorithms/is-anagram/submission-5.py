class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Check to ensure both strings are the same length
        if len(s) != len(t):
            return False

        # Initialize Hashmap
        countS, countT = {}, {}

        # Build the Hashmap
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
            # Compare characters in our hashmaps
        for c in countS:
            if countS[c] != countT.get(c, 0):
                return False
        return True
        