class Solution:
    def countArrangement(self, n: int) -> int:
        # Backtracking function to calculate valid arrangements
        def backtrack(pos, visited):
            # If all positions are filled, it is a valid arrangement
            if pos > n:
                return 1
            
            count = 0
            for i in range(1, n + 1):
                if not visited[i - 1] and (i % pos == 0 or pos % i == 0):
                    visited[i - 1] = True
                    count += backtrack(pos + 1, visited)  # Recurse for the next position
                    visited[i - 1] = False  # Backtrack
            
            return count
        
        # Initialize the visited list to track the numbers placed in the arrangement
        visited = [False] * n
        return backtrack(1, visited)


