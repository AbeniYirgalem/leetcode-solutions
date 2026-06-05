class Solution:
    def calculate(self, s: str) -> int:
        result = 0
        sign = 1
        number = 0
        stack = []

        for ch in s:
            if ch.isdigit():
                number = number * 10 + int(ch)
            elif ch in "+-":
                result += sign * number
                number = 0
                sign = 1 if ch == "+" else -1
            elif ch == "(":
                stack.append(result)
                stack.append(sign)
                result = 0
                sign = 1
            elif ch == ")":
                result += sign * number
                number = 0
                result *= stack.pop()
                result += stack.pop()

        result += sign * number
        return result


if __name__ == "__main__":
    sol = Solution()
    print(sol.calculate("1 + (2 - 3) + 4"))
    print(sol.calculate("2-1 + 2"))
    print(sol.calculate("(1+(4+5+2)-3)+(6+8)"))
