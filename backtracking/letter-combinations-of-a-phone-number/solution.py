from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        phone = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        result: List[str] = []

        def backtrack(index: int, path: List[str]) -> None:
            if index == len(digits):
                result.append("".join(path))
                return
            for ch in phone[digits[index]]:
                path.append(ch)
                backtrack(index + 1, path)
                path.pop()

        backtrack(0, [])
        return result


if __name__ == "__main__":
    sol = Solution()
    print(sol.letterCombinations("23"))
    print(sol.letterCombinations("7"))
    print(sol.letterCombinations(""))
