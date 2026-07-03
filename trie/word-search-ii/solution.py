from typing import List, Dict


class TrieNode:
    def __init__(self) -> None:
        self.children: Dict[str, "TrieNode"] = {}
        self.word: str = ""


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for word in words:
            node = root
            for ch in word:
                node = node.children.setdefault(ch, TrieNode())
            node.word = word

        rows, cols = len(board), len(board[0])
        result: List[str] = []

        def dfs(r: int, c: int, node: TrieNode) -> None:
            ch = board[r][c]
            if ch not in node.children:
                return
            next_node = node.children[ch]
            if next_node.word:
                result.append(next_node.word)
                next_node.word = ""

            board[r][c] = "#"
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] != "#":
                    dfs(nr, nc, next_node)
            board[r][c] = ch

            if not next_node.children:
                node.children.pop(ch, None)

        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root)

        return result


if __name__ == "__main__":
    sol = Solution()
    board = [
        ["o", "a", "a", "n"],
        ["e", "t", "a", "e"],
        ["i", "h", "k", "r"],
        ["i", "f", "l", "v"],
    ]
    print(sorted(sol.findWords(board, ["oath", "pea", "eat", "rain"])))
    print(sorted(sol.findWords([["a"]], ["a", "b"])) )
    print(sorted(sol.findWords([["a", "b"], ["c", "d"]], ["abcd"])) )
