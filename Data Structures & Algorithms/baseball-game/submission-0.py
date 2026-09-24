class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        n = len(operations)
        for i in range(n):
            if operations[i] == "+":
                stack.append(stack[-1] + stack[-2])
            elif operations[i] == "C":
                stack.pop()
            elif operations[i] == "D":
               stack.append(stack[-1] * 2)
            else:
                stack.append(int(operations[i]))
        return sum(stack)


        