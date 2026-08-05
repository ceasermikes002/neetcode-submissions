class Solution:
    def isValid(self, s: str) -> bool:
        # ── Step 1: Initialize a stack and a bracket map ────────────────
        # Stack to keep open brackets
        stack = []
        # Mapping for closing brackets to their corresponding open brackets
        bracket_map = {')': '(', '}': '{', ']': '['}

        # ── Step 2: Process each character in the string ───────────────
        for char in s:
            # If the character is a closing bracket
            if char in bracket_map:
                # Pop the stack if possible, otherwise use a dummy value '#'
                top_element = stack.pop() if stack else '#'
                
                # Check if the popped element matches the expected open bracket
                if bracket_map[char] != top_element:
                    return False
            else:
                # If it's an opening bracket, push onto the stack
                stack.append(char)

        # ── Step 3: Validate and return the result ────────────────────
        # If the stack is empty, all brackets were matched correctly
        return not stack