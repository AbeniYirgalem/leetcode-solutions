from typing import Dict


class TrieNode:
    def __init__(self) -> None:
        self.children: Dict[str, "TrieNode"] = {}
        self.is_word = False


class WordDictionary:
    def __init__(self) -> None:
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for ch in word:
            node = node.children.setdefault(ch, TrieNode())
        node.is_word = True

    def search(self, word: str) -> bool:
        def dfs(index: int, node: TrieNode) -> bool:
            if index == len(word):
                return node.is_word
            ch = word[index]
            if ch == ".":
                return any(dfs(index + 1, child) for child in node.children.values())
            if ch not in node.children:
                return False
            return dfs(index + 1, node.children[ch])

        return dfs(0, self.root)


if __name__ == "__main__":
    wd = WordDictionary()
    wd.addWord("bad")
    wd.addWord("dad")
    wd.addWord("mad")
    print(wd.search("pad"))
    print(wd.search("bad"))
    print(wd.search(".ad"))
    print(wd.search("b.."))
