class Solution {
    public int rob(int[] nums) {
        int length = nums.length;
        int prev2 = 0;
        int prev1 = nums[0];

        for(int i = 1;i<length;i++){
            int cur = (prev2+nums[i] > prev1) ? prev2+nums[i] : prev1;
            prev2 = prev1;
            prev1 = cur;
        }

        return prev1;

        
    }
}
