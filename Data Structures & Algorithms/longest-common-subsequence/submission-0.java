class Solution {
    public int longestCommonSubsequence(String text1, String text2) {
        int rows = text1.length() + 1;
        int cols = text2.length() + 1;

        int[][] dp = new int[rows][cols];

        for(int i = 0;i<rows;i++){
            dp[i][0] = 0;
        }
        for(int j = 0;j<cols;j++){
            dp[0][j] = 0;
        }
        for(int i = 1; i<rows;i++){
            for(int j = 1; j<cols;j++){
                dp[i][j] = Integer.MIN_VALUE;
            }
        }

        for(int i = 1; i<rows;i++){
            for(int j = 1; j<cols;j++){
                if(text1.charAt(i-1) == text2.charAt(j-1)){
                    dp[i][j] = 1 + dp[i-1][j-1];
                }else{
                    dp[i][j] = Math.max(dp[i-1][j], dp[i][j-1]);
                }
            }
        }
        return dp[rows-1][cols-1];
        
    }
}
