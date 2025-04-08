class UnionFind: 
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1]*n
        self.components = n
    
    def find(self, p):
        if p != self.parent[p]: 
            self.parent[p] = self.find(self.parent[p])
        return self.parent[p]
    
    def union(self, p, q):
        prt, qrt = self.find(p), self.find(q)
        if prt == qrt: return False 
        self.components -= 1
        if self.rank[prt] > self.rank[qrt]: prt, qrt = qrt, prt
        self.parent[prt] = qrt
        self.rank[qrt] += self.rank[qrt]
        return True 
    

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = UnionFind(n)
        for u, v in edges: uf.union(u, v)
        return uf.components
