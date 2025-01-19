class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        rows, cols = len(heightMap), len(heightMap[0])
        minheap = []

        for r in range(rows):
            for c in range(cols):
                if r in [0, rows-1] or c in [0, cols-1] : #border cells
                    heappush(minheap, (heightMap[r][c], r, c))
                    heightMap[r][c] = -1
        res = 0
        max_h = -1
        while minheap :
            h, r, c = heappop(minheap)
            max_h = max(max_h, h)
            res += max_h - h
            nei = [[r+1, c], [r-1, c], [r, c+1], [r, c-1]]
            for nr, nc in nei:
                if (nr < 0 or nr >= rows or nc < 0 or nc >= cols or heightMap[nr][nc] == -1):
                    continue
                heappush(minheap, (heightMap[nr][nc], nr, nc))
                heightMap[nr][nc] = -1
        return res
        

        
        
