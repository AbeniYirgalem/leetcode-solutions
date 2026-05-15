class Solution:
    def isValid(self, s: str) -> bool:
        match = {')': '(', ']': '[', '}': '{'}
        stack = []
        for ch in s:
            if ch in match:
                if not stack or stack[-1] != match[ch]:
                    return False
                stack.pop()
            else:
                stack.append(ch)
        return not stack

if __name__ == "__main__":
    sol = Solution()
    print(sol.isValid("()"))
    print(sol.isValid("(]"))
