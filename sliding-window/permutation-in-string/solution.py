class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        target = [0] * 26
        window = [0] * 26
        for ch in s1:
            target[ord(ch) - ord("a")] += 1

        for i, ch in enumerate(s2):
            window[ord(ch) - ord("a")] += 1
            if i >= len(s1):
                window[ord(s2[i - len(s1)]) - ord("a")] -= 1
            if window == target:
                return True
        return False


if __name__ == "__main__":
    sol = Solution()
    print(sol.checkInclusion("ab", "eidbaooo"))
    print(sol.checkInclusion("ab", "eidboaoo"))
    print(sol.checkInclusion("a", "a"))
