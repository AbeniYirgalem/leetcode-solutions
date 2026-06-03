class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = [0] * 26
        left = 0
        max_count = 0
        best = 0

        for right, ch in enumerate(s):
            idx = ord(ch) - ord("A")
            count[idx] += 1
            max_count = max(max_count, count[idx])

            while (right - left + 1) - max_count > k:
                count[ord(s[left]) - ord("A")] -= 1
                left += 1

            best = max(best, right - left + 1)
        return best


if __name__ == "__main__":
    sol = Solution()
    print(sol.characterReplacement("AABABBA", 1))
    print(sol.characterReplacement("ABAB", 2))
    print(sol.characterReplacement("A", 0))
