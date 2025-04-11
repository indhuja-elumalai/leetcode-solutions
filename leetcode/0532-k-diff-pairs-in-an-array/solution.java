class Solution {
    public int findPairs(int[] nums, int k) {
        if (k < 0) return 0; // No valid pairs for negative k

        int count = 0;
        
        // Sort the array to make it easier to find pairs
        Arrays.sort(nums);

        // Iterate through the array
        for (int i = 0; i < nums.length; i++) {
            // Skip duplicates for the first number in the pair
            if (i > 0 && nums[i] == nums[i - 1]) continue;

            // Look for the second number in the pair
            for (int j = i + 1; j < nums.length; j++) {
                // If the difference matches k, increment the count
                if (nums[j] - nums[i] == k) {
                    count++;
                    break; // No need to check further as we found one pair
                } else if (nums[j] - nums[i] > k) {
                    break; // No need to check further as the difference is too large
                }
            }
        }

        return count;
    }
}

