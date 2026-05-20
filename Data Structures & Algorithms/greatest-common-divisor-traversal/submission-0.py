class UnionFind:
    def __init__(self,n):
        self.parent = list(range(n))
        self.size = [1]*n

    def find(self, x):
        while x != self.parent[x]:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self,a,b):
        pa,pb = self.find(a), self.find(b)
        if pa == pb: return False
        if self.size[pa] < self.size[pb]: pa,pb = pb,pa
        self.parent[pb] = pa
        self.size[pa] += self.size[pb]

class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        n = len(nums)
        if n == 1:
            return True

        # Any 1 makes connection impossible (no prime factors)
        if any(num == 1 for num in nums):
            return False

        max_val = max(nums)

        # Smallest prime factor sieve up to max_val
        spf = list(range(max_val + 1))
        p = 2
        while p * p <= max_val:
            if spf[p] == p:  # p is prime
                for multiple in range(p * p, max_val + 1, p):
                    if spf[multiple] == multiple:
                        spf[multiple] = p
            p += 1

        # DSU: 0..n-1 for indices, n..n+max_val for prime nodes
        uf = UnionFind(n + max_val + 1)

        # Connect each index to its prime factors
        for i, num in enumerate(nums):
            x = num
            last_prime = -1
            while x > 1:
                prime = spf[x]
                if prime == x:  # x itself is prime
                    pass
                # Union index i with prime node (offset by n)
                uf.union(i, n + prime)
                # Remove all occurrences of this prime
                while x % prime == 0:
                    x //= prime

        # Check if all indices share the same root
        root0 = uf.find(0)
        for i in range(1, n):
            if uf.find(i) != root0:
                return False
        return True