class Solution:
    def combinationSum2(self, candidates, target):
        result = []
        candidates.sort()  # Sort the list to handle duplicates easily
        
        def backtrack(start, target, current_combination):
            # If the target is 0, we've found a valid combination
            if target == 0:
                result.append(list(current_combination))
                return
            
            # Iterate through the candidates starting from 'start'
            for i in range(start, len(candidates)):
                # Skip duplicates
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                
                # If the candidate is greater than the remaining target, break the loop
                if candidates[i] > target:
                    break
                
                # Choose the candidate and recurse
                current_combination.append(candidates[i])
                backtrack(i + 1, target - candidates[i], current_combination)  # Move forward with next numbers
                current_combination.pop()  # Backtrack, remove the last number

        # Start the backtracking with an empty combination
        backtrack(0, target, [])
        
        return result

