class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""

        start = 0
        end = 0

        def expand(left: int, right: int) -> None:
            nonlocal start, end
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            left += 1
            right -= 1
            if right - left > end - start:
                start, end = left, right

        for i in range(len(s)):
            expand(i, i)
            expand(i, i + 1)

        return s[start : end + 1]


if __name__ == "__main__":
    sol = Solution()
    print(sol.longestPalindrome("babad"))
    print(sol.longestPalindrome("cbbd"))
    print(sol.longestPalindrome("a"))
