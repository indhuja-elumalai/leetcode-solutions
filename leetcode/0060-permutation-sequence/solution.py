import math
class Solution:
    def getPermutation(self, n: int, k: int) -> str:

        # Create a list of numbers to get permutations from
        numbers = list(range(1, n + 1))
        
        # Convert k to 0-based index
        k -= 1
        
        # To store the result
        result = []
        
        # Calculate factorials from 1 to n-1
        for i in range(n, 0, -1):
            fact = math.factorial(i - 1)  # (i-1)!
            
            # Find the index of the current number
            index = k // fact
            result.append(str(numbers.pop(index)))  # Add the number at index to the result
            
            # Update k for the next iteration
            k %= fact
        
        # Join the result as a string and return
        return ''.join(result)

