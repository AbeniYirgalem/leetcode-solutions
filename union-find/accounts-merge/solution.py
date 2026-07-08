from typing import List, Dict


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        parent: Dict[str, str] = {}
        owner: Dict[str, str] = {}

        def find(x: str) -> str:
            while x != parent[x]:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(a: str, b: str) -> None:
            root_a = find(a)
            root_b = find(b)
            if root_a != root_b:
                parent[root_b] = root_a

        for account in accounts:
            name = account[0]
            first_email = account[1]
            for email in account[1:]:
                if email not in parent:
                    parent[email] = email
                owner[email] = name
                union(first_email, email)

        groups: Dict[str, List[str]] = {}
        for email in parent:
            root = find(email)
            groups.setdefault(root, []).append(email)

        result: List[List[str]] = []
        for root, emails in groups.items():
            result.append([owner[root]] + sorted(emails))
        return result


if __name__ == "__main__":
    sol = Solution()
    accounts = [
        ["John", "johnsmith@mail.com", "john00@mail.com"],
        ["John", "johnnybravo@mail.com"],
        ["John", "johnsmith@mail.com", "john_newyork@mail.com"],
        ["Mary", "mary@mail.com"],
    ]
    print(sol.accountsMerge(accounts))
    print(sol.accountsMerge([["Alex", "a@mail.com"], ["Alex", "a@mail.com", "b@mail.com"]]))
    print(sol.accountsMerge([["Bob", "b@mail.com"], ["Bob", "c@mail.com"]]))
