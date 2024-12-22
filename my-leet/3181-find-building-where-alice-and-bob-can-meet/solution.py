class Solution:
    def leftmostBuildingQueries(self, heights, queries):
        n, q = len(heights), len(queries)
        r = [-1] * q
        d = [[] for _ in range(n)]
        pq = []

        for i in range(q):
            a, b = queries[i]
            if a > b:
                a, b = b, a
            if a == b or heights[a] < heights[b]:
                r[i] = b
            else:
                d[b].append((heights[a], i))

        for i in range(n):
            for query in d[i]:
                heapq.heappush(pq, query)
            while pq and pq[0][0] < heights[i]:
                r[pq[0][1]] = i
                heapq.heappop(pq)

        return r
