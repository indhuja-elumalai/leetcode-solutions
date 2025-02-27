class Solution:
    def getMaximumGold(self, grid):
        rows, cols = len(grid), len(grid[0])  # Get the dimensions of the grid
        max_gold = 0  # Variable to store the maximum gold we can collect

        # Backtracking function to explore the grid
        def backtrack(r, c):
            # If out of bounds or no gold in the cell, return 0
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == 0:
                return 0
            
            gold = grid[r][c]  # Collect the gold in the current cell
            grid[r][c] = 0  # Mark the current cell as visited

            # Explore all four directions: down, up, right, left
            collected_gold = gold + max(
                backtrack(r + 1, c),  # Move down
                backtrack(r - 1, c),  # Move up
                backtrack(r, c + 1),  # Move right
                backtrack(r, c - 1)   # Move left
            )

            grid[r][c] = gold  # Backtrack: restore the gold in the current cell
            return collected_gold

        # Check all cells in the grid
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] > 0:  # If the cell has gold
                    max_gold = max(max_gold, backtrack(r, c))  # Update the maximum gold collected

        return max_gold
