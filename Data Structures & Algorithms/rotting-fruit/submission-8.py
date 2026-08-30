class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        q = deque()
        fresh = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    q.append((i, j))
                elif grid[i][j] == 1:
                    fresh += 1
        
        mins = 0
        while q:
            for i in range(len(q)):
                x, y = q.popleft()
                for dx, dy in directions:
                    nx, ny = x+dx, y+dy
                    if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 1:
                        grid[nx][ny] = 2
                        q.append((nx, ny))
                        fresh -= 1
            if q:
                mins += 1
            
        
        return -1 if fresh != 0 else mins 

        
        
        
