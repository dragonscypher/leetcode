class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        numRows = len(grid)
        lastRow = numRows - 1
        numCols = len(grid[0])
        lastCol = numCols - 1

        def getNeigbors(row, col):
            nonlocal grid, lastRow, lastCol
            v = grid[row][col]
            if row > 0:
                yield row - 1, col, int(v != 4)
            if row < lastRow:
                yield row + 1, col, int(v != 3)
            if col > 0:
                yield row, col - 1, int(v != 2)
            if col < lastCol:
                yield row, col + 1, int(v != 1)


        costs = [[numRows * numCols] * numCols for _ in range(numRows)]
        costs[0][0] = 0

        pq = [(0, 0, 0)]

        while pq:
            curCost, row, col = heappop(pq)
            if costs[row][col] == curCost:
                if row == lastRow and col == lastCol:
                    return curCost
                
                for nextRow, nextCol, nextCost in getNeigbors(row, col):
                    nextCost += curCost
                    if costs[nextRow][nextCol] > nextCost:
                        costs[nextRow][nextCol] = nextCost
                        heappush(pq, (nextCost, nextRow, nextCol))




        return costs[-1][-1]
