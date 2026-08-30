class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        rows, cols = len(grid), len(grid[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def dfs(x, y):
            if not (0 <= x < rows and 0 <= y < cols):
                return 0
            if grid[x][y] != 1:
                return 0
            area = 1
            grid[x][y] = 0

            for dx, dy in directions:
                area += dfs(dx+x, dy+y)
            return area


        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    area = dfs(i, j)
                    max_area = max(area, max_area)
        return max_area

