class Solution {
    public int findJudge(int n, int[][] trust) {
        int[] trustScore = new int[n + 1]; // Index 0 unused

        for (int[] t : trust) {
            trustScore[t[0]]--; // Person trusts someone -> reduce score
            trustScore[t[1]]++; // Person is trusted -> increase score
        }

        for (int i = 1; i <= n; i++) {
            if (trustScore[i] == n - 1) {
                return i; // Found the judge
            }
        }

        return -1; // No judge found
    }
}

