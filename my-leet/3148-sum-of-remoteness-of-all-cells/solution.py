class Solution:
    def sumRemoteness(self, grid: List[List[int]]) -> int:
        N = len(grid)
        total = 0

        ans = 0


        seen = [[0] * N for _ in range(N)]
        for i in range(N):
            for j in range(N):
                if grid[i][j] != -1:
                    total += grid[i][j]

        
        def bfs(start):
            nonlocal ans

            group = []


            q = deque([start])

            while q:
                x, y = q.popleft()
                group.append(grid[x][y])

                directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]

                for dx, dy in directions:
                    nx, ny = x + dx, y + dy

                    if not (0 <= nx < N) or not (0 <= ny < N):
                        continue

                    if seen[nx][ny]:
                        continue
                    
                    if grid[nx][ny] == -1:
                        continue

                    seen[nx][ny] = 1
                    q.append((nx, ny))
            s = sum(group)
            # print(total, s, len(group))
            ans += (total - s) * len(group)

        for i in range(N):
            for j in range(N):
                if not seen[i][j] and grid[i][j] != -1:
                    seen[i][j] = 1
                    bfs((i, j))
                    

    
        return ans
