class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        
        start = (0, 0)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "*":
                    start = (i, j)
                    break

        directions = [(0,1), (1, 0), (-1, 0), (0, -1)]
        queue = deque([(start[0], start[1], 0)])
        seen = set((start[0], start[1]))
        sh = inf

        while queue:

            row, col, path = queue.popleft()

            if (row, col) in seen:
                continue

            seen.add((row, col))

            for r, c in directions:

                if 0 <= r + row < len(grid) and 0 <= c + col < len(grid[0]):
                    if grid[r + row][c + col] == "#":
                        sh = min(sh, path + 1)
                        continue

                    if grid[r + row][c + col] == "X":
                        continue
                    else:
                        queue.append((r + row, col + c, path + 1))
        print(sh)
                        
        return sh if sh != inf else -1

        
        
