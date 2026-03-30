class Solution {

    public int coinChange(int[] coins, int amount) {

        int[] dp = new int[amount+1];
        dp[0] = 0;
        for(int i = 1; i<= amount;i++){
            dp[i] = Integer.MAX_VALUE;
        }

        for (int j = 1; j<= amount; j++){
            for(int coin : coins){
                if(coin <= j){
                    int subproblem = dp[j-coin];
                    if(subproblem != Integer.MAX_VALUE){
                        dp[j] = Math.min(dp[j], dp[j-coin]+1);
                    }
                }                
            }
        }

        if (dp[amount] == Integer.MAX_VALUE){
            return -1;
        }
        return dp[amount];
        
    }
}
