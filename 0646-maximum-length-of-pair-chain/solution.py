class Solution:
    def findLongestChain(self, pairs):
        # Step 1: Sort pairs by the second element of each pair (right part)
        pairs.sort(key=lambda x: x[1])
        
        # Step 2: Initialize variables
        current_end = float('-inf')  # To keep track of the end of the current chain
        chain_length = 0  # The length of the longest chain
        
        # Step 3: Iterate through each pair
        for pair in pairs:
            if pair[0] > current_end:  # If the current pair can follow the previous one
                current_end = pair[1]  # Update the end of the current chain
                chain_length += 1  # Increase the length of the chain
        
        # Step 4: Return the length of the longest chain
        return chain_length
