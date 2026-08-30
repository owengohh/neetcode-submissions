class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        rows, cols = len(board), len(board[0])

        def bt(i, x, y):
            if i == len(word):
                return True
            if not (0 <= x < rows and 0 <= y < cols) or board[x][y] != word[i]:
                return False
            
            tmp = board[x][y]
            board[x][y] = "#"
            
            for dx, dy in directions:
                nx, ny = dx+x, dy+y
                if bt(i+1, nx, ny):
                    return True
                
            board[x][y] = tmp
            return False
        
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == word[0]:
                    if bt(0, i, j):
                        return True
        return False
