class Solution {
    public int findContentChildren(int[] g, int[] s) {
        // Manual sort using Selection Sort
        selectionSort(g);
        selectionSort(s);

        int i = 0; // Pointer for children
        int j = 0; // Pointer for cookies
        int count = 0;

        // Try to satisfy each child with the smallest suitable cookie
        while (i < g.length && j < s.length) {
            if (s[j] >= g[i]) {
                count++; // Child is content
                i++;     // Move to next child
            }
            j++; // Always move to next cookie
        }

        return count;
    }

    // Manual selection sort implementation
    private void selectionSort(int[] arr) {
        int n = arr.length;
        for (int i = 0; i < n - 1; i++) {
            int minIdx = i;
            for (int j = i + 1; j < n; j++) {
                if (arr[j] < arr[minIdx]) {
                    minIdx = j;
                }
            }
            // Swap arr[i] and arr[minIdx]
            int temp = arr[i];
            arr[i] = arr[minIdx];
            arr[minIdx] = temp;
        }
    }
}

