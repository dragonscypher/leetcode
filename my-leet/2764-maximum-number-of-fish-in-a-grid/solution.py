class Solution:
    def solve(self, i, j, grid):
        if i < 0 or i >= self.m or j < 0 or j >= self.n or grid[i][j] == 0:
            return 0
        temp = grid[i][j]
        grid[i][j] = 0
        temp += self.solve(i + 1, j, grid)
        temp += self.solve(i - 1, j, grid)
        temp += self.solve(i, j + 1, grid)
        temp += self.solve(i, j - 1, grid)
        return temp

    def findMaxFish(self, grid):
        self.m, self.n = len(grid), len(grid[0])
        ans = 0
        for i in range(self.m):
            for j in range(self.n):
                if grid[i][j] != 0:
                    ans = max(ans, self.solve(i, j, grid))
        return ans
