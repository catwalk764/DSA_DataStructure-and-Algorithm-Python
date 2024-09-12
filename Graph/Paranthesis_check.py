#!/usr/bin/env python3

class Solution(object):
    def valid_check(self, s):
        # Stack to keep track of opening brackets
        stack = []
        
        # Mapping of closing to opening brackets
        mapping = {")": "(", "}": "{", "]": "["}

        # Loop through each character in the string
        for char in s:
            # Check if the character is a closing bracket
            if char in mapping:
                # If the stack is not empty, pop the top element
                if stack:
                    top_element = stack.pop()
                else:
                    # If the stack is empty, assign a special value
                    top_element = '#'

                # Check if the popped element matches the corresponding opening bracket
                if mapping[char] != top_element:
                    return False  # Mismatch found

            else:
                # If it's an opening bracket, push it onto the stack
                stack.append(char)

        # If the stack is empty, all brackets were matched
        return len(stack) == 0


solution = Solution()
s = "(}"
result = solution.valid_check(s)
print(result)