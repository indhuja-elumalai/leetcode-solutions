class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result = []
        
        def backtrack(row, board, columns, diag1, diag2):
            if row == n:
                result.append(["".join(row) for row in board])
                return
            
            for col in range(n):
                if col in columns or (row - col) in diag1 or (row + col) in diag2:
                    continue
                
                # Place the queen
                board[row][col] = 'Q'
                columns.add(col)
                diag1.add(row - col)
                diag2.add(row + col)
                
                # Recurse for the next row
                backtrack(row + 1, board, columns, diag1, diag2)
                
                # Backtrack, remove the queen
                board[row][col] = '.'
                columns.remove(col)
                diag1.remove(row - col)
                diag2.remove(row + col)

        # Initialize the board and sets for columns and diagonals
        board = [['.' for _ in range(n)] for _ in range(n)]
        columns = set()
        diag1 = set()
        diag2 = set()
        
        # Start the backtracking from the first row
        backtrack(0, board, columns, diag1, diag2)
        
        return result
