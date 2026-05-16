from typing import List


class Codec:
    def encode(self, strs: List[str]) -> str:
        return "".join(f"{len(s)}#{s}" for s in strs)

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            j += 1
            result.append(s[j : j + length])
            i = j + length
        return result

if __name__ == "__main__":
    codec = Codec()
    encoded = codec.encode(["lint", "code", "love", "you"])
    print(encoded)
    print(codec.decode(encoded))
