class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        p_seen = set()
        p_q = deque()

        a_seen = set()
        a_q = deque()

        for i in range(cols):
            p_seen.add((0, i))
            p_q.append((0, i))
        
        for i in range(1, rows):
            p_seen.add((i, 0))
            p_q.append((i, 0))
        
        for i in range(cols):
            a_seen.add((rows-1, i))
            a_q.append((rows-1, i))
        
        for i in range(rows-1):
            a_seen.add((i, cols-1))
            a_q.append((i, cols-1))
        
        def dfs(seen, q):
            coords = set()
            while q:
                x, y = q.popleft()
                coords.add((x, y))
                for dx, dy in directions:
                    nx, ny = dx+x, dy+y
                    if (0 <= nx < rows and 0 <= ny < cols and heights[nx][ny] >= heights[x][y] and (nx, ny) not in seen):
                        seen.add((nx, ny))
                        q.append((nx, ny))
            return coords
        
        p_coords = dfs(p_seen, p_q)
        a_coords = dfs(a_seen, a_q)
        return list(p_coords.intersection(a_coords))
