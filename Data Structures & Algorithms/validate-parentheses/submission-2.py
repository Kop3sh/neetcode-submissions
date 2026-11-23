class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        adj = {'(': ')', '[':']', '{':'}'}

        for c in s:
            if c in {'(', '[', '{'}:
                stack.append(c)
            if c in {')', ']', '}'}:
                if stack and adj[stack[-1]] == c:
                    stack.pop()
                else:
                    return False
        return len(stack) == 0
        