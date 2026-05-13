from collections import defaultdict, deque
from typing import List


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        word_len = len(beginWord)
        patterns = defaultdict(list)
        for word in wordList:
            for i in range(word_len):
                patterns[word[:i] + "*" + word[i + 1 :]].append(word)
        queue = deque([(beginWord, 1)])
        visited = {beginWord}
        while queue:
            word, steps = queue.popleft()
            if word == endWord:
                return steps
            for i in range(word_len):
                pattern = word[:i] + "*" + word[i + 1 :]
                for neighbor in patterns.get(pattern, []):
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append((neighbor, steps + 1))
                patterns[pattern] = []
        return 0

if __name__ == "__main__":
    sol = Solution()
    print(sol.ladderLength("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
    print(sol.ladderLength("hit", "cog", ["hot", "dot", "dog", "lot", "log"]))
