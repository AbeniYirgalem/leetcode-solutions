from typing import List


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        result: List[str] = []

        def backtrack(index: int, parts: List[str]) -> None:
            if len(parts) == 4:
                if index == len(s):
                    result.append(".".join(parts))
                return
            remaining = len(s) - index
            if remaining < (4 - len(parts)) or remaining > 3 * (4 - len(parts)):
                return
            for length in range(1, 4):
                if index + length > len(s):
                    break
                chunk = s[index : index + length]
                if (chunk.startswith("0") and len(chunk) > 1) or int(chunk) > 255:
                    continue
                parts.append(chunk)
                backtrack(index + length, parts)
                parts.pop()

        backtrack(0, [])
        return result


if __name__ == "__main__":
    sol = Solution()
    print(sol.restoreIpAddresses("25525511135"))
    print(sol.restoreIpAddresses("0000"))
    print(sol.restoreIpAddresses("1111"))
