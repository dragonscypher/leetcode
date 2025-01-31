class Disjoint_Set:
    
    def __init__(self,v):
        self.v=v
        self.size = [1]*v
        self.parent = [i for i in range(v)]
        
    def ultimate_parent(self, u):
        while u != self.parent[u]:
            self.parent[u] = self.parent[self.parent[u]]  # Path compression
            u = self.parent[u]
        return u

    
    def unionBySize(self,u,v):
        ult_u=self.ultimate_parent(u)
        ult_v=self.ultimate_parent(v)
        if ult_u==ult_v:
            return
        if self.size[ult_u]>self.size[ult_v]:
            self.parent[ult_v]=ult_u
            self.size[ult_u]+=self.size[ult_v]
        else:
            self.parent[ult_u]=ult_v
            self.size[ult_v]+=self.size[ult_u]

class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n=len(grid)
        dsu=Disjoint_Set(n*n+1)
        dirs=[(-1,0),(0,-1),(0,1),(1,0)]
        for i in range(n):
            for j in range(n):
                if grid[i][j]==1:
                    cur_val=i*n+j
                    for k in dirs:
                        x=i+k[0]
                        y=j+k[1]
                        if 0<=x<n and 0<=y<n and grid[x][y]==1:
                            adj_val=x*n+y
                            dsu.unionBySize(cur_val,adj_val)
        ans=max(dsu.size)
        for i in range(n):
            for j in range(n):
                if grid[i][j]==0:
                    temp=0
                    uset=set()
                    for k in dirs:    
                        dx=i+k[0]
                        dy=j+k[1]
                        val=dx*n+dy
                        if 0<=dx<n and 0<=dy<n and grid[dx][dy]==1:
                            uset.add(dsu.ultimate_parent(val))
                    temp=1
                    for p in uset:
                        temp+=dsu.size[p]
                    if temp>ans:
                        ans=temp
        return ans

                    
                    
                    








            



        

        
