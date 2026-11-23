from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()

        for c in s:
            # print(stack)
            # stack.append(c)
            # if stack[-1] and stack[-1] == '[' and c == ']':
            #     stack.pop()
            #     stack.pop()
            # elif stack[-1] and stack[-1] == '{' and c == '}':
            #     stack.pop()
            #     stack.pop()
            # elif stack[-1] and stack[-1] == '(' and c == ')':
            #     stack.pop()
            #     stack.pop()

            if len(stack) == 0 and c in ')]}':
                return False
            elif len(stack) != 0 and c in ')]}':
                if c == ')' and stack[-1] == '(':
                    stack.pop()
                elif c == ']' and stack[-1] == '[':
                    stack.pop()
                elif c == '}' and stack[-1] == '{':
                    stack.pop()
                else:
                    stack.append(c)
            elif c in '([{':
                stack.append(c)

        
        return len(stack) == 0

        