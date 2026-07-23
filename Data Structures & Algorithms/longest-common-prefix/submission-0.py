class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""  # Case for empty input list
        
        # Assume the first string is the common prefix
        prefix = strs[0]
        
        # Compare the assumed prefix with each string
        for string in strs[1:]:
            # Check current string against current prefix
            while string[:len(prefix)] != prefix:
                prefix = prefix[:-1]  # Reduce prefix by one character
                if not prefix:
                    return ""  # Return immediately if no common prefix left
        
        return prefix  # Return the determined common prefix