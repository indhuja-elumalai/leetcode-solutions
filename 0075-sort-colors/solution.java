class Solution {
    public void sortColors(int[] nums) {
        int low = 0, mid = 0, high = nums.length - 1;
        
        // Traverse the array
        while (mid <= high) {
            switch (nums[mid]) {
                case 0:  // If the element is 0, swap with low pointer
                    swap(nums, low, mid);
                    low++;
                    mid++;
                    break;
                case 1:  // If the element is 1, just move the mid pointer
                    mid++;
                    break;
                case 2:  // If the element is 2, swap with high pointer
                    swap(nums, mid, high);
                    high--;
                    break;
            }
        }
    }
    
    // Helper function to swap elements at indices i and j
    private void swap(int[] nums, int i, int j) {
        int temp = nums[i];
        nums[i] = nums[j];
        nums[j] = temp;
    }
}

