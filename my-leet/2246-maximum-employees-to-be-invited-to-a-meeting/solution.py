class Solution:
    def maximumInvitations(self, favorite: List[int]) -> int:
        n = len(favorite)
        prev = [[] for _ in range(n)]
        for i, f in enumerate(favorite):
            prev[f].append(i)

        loop_len = [0]*n
        max_prefix = [0]*n 
        def set_max_prefix(h: int):
            L = loop_len[h]
            q = deque(p for p in prev[h] if loop_len[p] == 0)
            while q:
                max_prefix[h] += 1

                for _ in range(len(q)):
                    p = q.popleft()
                    loop_len[p] = -1 
                    q.extend(prev[p]) 
        for i in range(n):
            if loop_len[i]: continue
            slow = favorite[i]
            fast = favorite[slow]
            while slow != fast:
                slow = favorite[slow]
                fast = favorite[favorite[fast]]
            L = 1
            slow = favorite[slow]
            while slow != fast:
                L += 1
                slow = favorite[slow]
            for _ in range(L):
                loop_len[slow] = L
                slow = favorite[slow]

            for _ in range(L):
                set_max_prefix(slow)
                slow = favorite[slow]

        most_oneloop = max((loop_len[i] for i in range(n) if loop_len[i] > 2), default=0)

        most_dimers = 0
        for i in range(n):
            if loop_len[i] == 2:
                most_dimers += 2 + max_prefix[i] + max_prefix[favorite[i]]
        most_dimers //= 2 
        return max(most_oneloop, most_dimers)
