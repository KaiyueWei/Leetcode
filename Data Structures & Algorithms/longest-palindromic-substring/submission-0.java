class Solution {

    public int helper(String s, int left, int right, int n){
       while(left >= 0 && right <= n - 1 && s.charAt(left) == s.charAt(right)){
            left--;
            right++;
       } 
       return right - left - 1;
    }

    public String longestPalindrome(String s) {
        int n = s.length();
        int start = 0;
        int end = 0;
        for(int i = 0; i<n;i++){
            int len1 = helper(s, i, i+1, n);
            int len2 = helper(s, i, i, n);
            int len = Math.max(len1, len2);
            if(len > end - start){
                start = i - (len-1)/2;
                end = i + len/2;
            }
        }
        return s.substring(start, end+1);
    }
}
