from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict)
        max_len = max((len(w) for w in word_set), default=0)
        dp = [False] * (len(s) + 1)
        dp[0] = True

        for i in range(1, len(s) + 1):
            for length in range(1, min(max_len, i) + 1):
                if dp[i - length] and s[i - length : i] in word_set:
                    dp[i] = True
                    break
        return dp[-1]


if __name__ == "__main__":
    sol = Solution()
    print(sol.wordBreak("leetcode", ["leet", "code"]))
    print(sol.wordBreak("applepenapple", ["apple", "pen"]))
    print(sol.wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]))
