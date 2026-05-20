class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        parent = [i for i in range(len(accounts))]
        size = [1] * len(accounts)

        def find(x):
            if parent[x] != x: parent[x] = find(parent[x])
            return parent[x]

        def union(a,b):
            rootA = find(a)
            rootB = find(b)
            if rootA == rootB: return
            if size[rootA] < size[rootB]:
                parent[rootA] = rootB
                size[rootB] += size[rootA]
            else:
                parent[rootB] = rootA
                size[rootA] += size[rootB]
        
        emailToAcc = {}
        for i, acc in enumerate(accounts):
            name = acc[0]
            for email in acc[1:]:
                if email in emailToAcc: union(i, emailToAcc[email])
                else: emailToAcc[email] = i
        
        rootToEmails = defaultdict(set)

        for i, acc in enumerate(accounts):
            root = find(i)
            for email in acc[1:]:
                rootToEmails[root].add(email)

        res = []
        for root, emails in rootToEmails.items():
            name = accounts[root][0]
            merged = [name] + sorted(emails)
            res.append(merged)
        
        return res