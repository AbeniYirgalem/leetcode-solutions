from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []
        target = [0] * 26
        window = [0] * 26
        for ch in p:
            target[ord(ch) - ord("a")] += 1

        result: List[int] = []
        for i, ch in enumerate(s):
            window[ord(ch) - ord("a")] += 1
            if i >= len(p):
                window[ord(s[i - len(p)]) - ord("a")] -= 1
            if window == target:
                result.append(i - len(p) + 1)
        return result


if __name__ == "__main__":
    sol = Solution()
    print(sol.findAnagrams("cbaebabacd", "abc"))
    print(sol.findAnagrams("abab", "ab"))
    print(sol.findAnagrams("a", "ab"))
