from collections import Counter


class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        count = Counter(tiles)

        def backtrack() -> int:
            total = 0
            for ch in list(count.keys()):
                if count[ch] == 0:
                    continue
                total += 1
                count[ch] -= 1
                total += backtrack()
                count[ch] += 1
            return total

        return backtrack()


if __name__ == "__main__":
    sol = Solution()
    print(sol.numTilePossibilities("AAB"))
    print(sol.numTilePossibilities("AAABBC"))
    print(sol.numTilePossibilities("V"))
