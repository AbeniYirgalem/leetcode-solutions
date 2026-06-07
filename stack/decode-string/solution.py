class Solution:
    def decodeString(self, s: str) -> str:
        count_stack = []
        string_stack = []
        current = []
        k = 0

        for ch in s:
            if ch.isdigit():
                k = k * 10 + int(ch)
            elif ch == "[":
                count_stack.append(k)
                string_stack.append("".join(current))
                current = []
                k = 0
            elif ch == "]":
                repeat = count_stack.pop()
                prev = string_stack.pop()
                current = list(prev + "".join(current) * repeat)
            else:
                current.append(ch)

        return "".join(current)


if __name__ == "__main__":
    sol = Solution()
    print(sol.decodeString("3[a]2[bc]"))
    print(sol.decodeString("3[a2[c]]"))
    print(sol.decodeString("2[abc]3[cd]ef"))
