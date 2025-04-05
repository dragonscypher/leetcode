class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        houses = []
        can_reach = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    grid[i][j] = "1"
                    houses.append((i, j))
                elif grid[i][j] == 2:
                    grid[i][j] = "2"
        for x, y in houses:
            q = deque([(x, y, 0)])
            visit = set([(x, y)])
            while q:
                curr_x, curr_y, dist = q.popleft()
                for dx, dy in directions:
                    nxt_x, nxt_y = curr_x + dx, curr_y + dy
                    if (
                        0 <= nxt_x < m
                        and 0 <= nxt_y < n
                        and (nxt_x, nxt_y) not in visit
                        and isinstance(grid[nxt_x][nxt_y], int)
                    ):
                        can_reach[nxt_x][nxt_y] += 1
                        visit.add((nxt_x, nxt_y))
                        q.append((nxt_x, nxt_y, dist + 1))
                        grid[nxt_x][nxt_y] += dist + 1
        res = float("inf")
        for i in range(m):
            for j in range(n):
                if isinstance(grid[i][j], int) and can_reach[i][j] == len(houses):
                    res = min(res, grid[i][j])
        if res == float("inf"):
            return -1
        return res

