class Solution {
    public int climbStairs(int n) {
        int[] dp = new int[n+1];

        int step2 = 1;
        int step1 = 1;

        for(int i = 2; i<=n;i++){
            int cur = step2 + step1;
            step2 = step1;
            step1 = cur;
        }

        return step1;
        
    }
}
