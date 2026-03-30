class Solution {
    public int longestCommonSubsequence(String text1, String text2) {
        int text1Len = text1.length();
        int text2Len = text2.length();

        int[] prev = new int[text2Len+1];
        int[] cur = new int[text2Len+1];

        cur[0] = 0;
        for(int i = 0;i<text2Len+1;i++){
            prev[i] = 0;
        }

        for(int i = 1; i<=text1Len;i++){
            for(int j = 1; j<=text2Len;j++){
                if(text1.charAt(i-1) == text2.charAt(j-1)){
                    cur[j] = 1 + prev[j-1];
                }else{
                    cur[j] = Math.max(cur[j-1], prev[j]);
                }
            }
            int[] temp = prev;
            prev = cur;
            cur = temp;
        }
        return prev[text2Len];
        
    }
}
