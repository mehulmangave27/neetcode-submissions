class Solution:
    def isValid(self, s: str) -> bool:
        closetoopen = {")" : "(", "]" : "[", "}" : "{"}
        stack = []

        for i in s:
            if i in closetoopen:
                if stack and stack[-1] == closetoopen[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        return True if len(stack) == 0 else False