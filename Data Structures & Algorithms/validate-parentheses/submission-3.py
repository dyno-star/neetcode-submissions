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
                if not stack or stack.pop() != valid[char]:
                    return False
                    
        return not stack