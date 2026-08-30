class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        rows, cols = len(heights), len(heights[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        a_seen = set()
        a_q = deque()

        p_seen = set()
        p_q = deque()

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

        def bfs(que, visited):
            coords = set()
            while que:
                x, y = que.popleft()
                coords.add((x, y))
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if (0 <= nx < rows and 0 <= ny < cols and heights[nx][ny] >= heights[x][y] and (nx, ny) not in visited):
                        que.append((nx, ny))
                        visited.add((nx, ny))
            return coords
        
        coords_p = bfs(p_q, p_seen)
        coords_a = bfs(a_q, a_seen)

        return list(coords_p.intersection(coords_a))
