class Solution:
    def simplifyPath(self, path: str) -> str:
        parts = path.split("/")
        stack = []
        for part in parts:
            if part == "" or part == ".":
                continue
            if part == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(part)
        return "/" + "/".join(stack)


if __name__ == "__main__":
    sol = Solution()
    print(sol.simplifyPath("/a/./b/../../c/"))
    print(sol.simplifyPath("/../"))
    print(sol.simplifyPath("/home//foo/"))
