class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        if not grid: return

        rows, cols = len(grid), len(grid[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        q = deque()

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    q.append((i, j))
        while q:
            x, y = q.popleft()
            for dx,dy in directions:
                nx, ny = x+dx, y+dy
                if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] != -1:
                    if grid[nx][ny] > grid[x][y] + 1:
                        grid[nx][ny] = grid[x][y] + 1
                        q.append((nx, ny))
                            
                