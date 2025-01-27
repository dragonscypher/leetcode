from functools import cache

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        rev = [[] for _ in range(numCourses)]
        for i, j in prerequisites:
            rev[j].append(i)
        
        @cache
        def dfs(s):
            seen = [False] * numCourses
            seen[s] = True
            stack = [s]
            while stack:
                u = stack.pop()
                for v in rev[u]:
                    if seen[v]:
                        continue
                    seen[v] = True
                    stack.append(v)
            return seen

        ans = []
        for u, v in queries:
            prereq = dfs(v)
            ans.append(prereq[u])
        return ans
