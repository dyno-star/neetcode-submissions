class Solution:
    def isValid(self, s: str) -> bool:
        valid = {
            ')':'(',
            '}': '{',
            ']': '['
        }
        stack = []
        for char in s:
            if char in valid.values():
                stack.append(char)
            if char in valid.keys():
                if not stack or stack[-1] != valid[char]:
                    return False
                stack.pop()   
        return not stack