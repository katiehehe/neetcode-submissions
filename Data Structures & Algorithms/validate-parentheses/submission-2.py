class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dict1 = {'(': 0, '{': 1, '[': 2}
        dict2 = {')': 0, '}': 1, ']': 2}
        for c in s:
            if c == '(' or c == '{' or c == '[':
                stack.append(c)
            else:
                if not stack:
                    return False
                if dict2[c] != dict1[stack[-1]]:
                    return False
                stack.pop()
        if stack:
            return False
        return True