class Solution {
    public int robHelper(int[] nums, int left, int right){
        // base case
        if(left==right){
            return nums[left];
        }
        // dp
        int prev2 = nums[left];
        int prev1 = Math.max(nums[left], nums[left+1]);

        for(int i = left + 2;i<=right;i++){
            int cur = Math.max(prev2+nums[i], prev1);
            prev2 = prev1;
            prev1 = cur;
        }

        return prev1;

    }
    public int rob(int[] nums) {

        int n = nums.length;

        if(n==0){
            return 0;
        }
        if(n==1){
            return nums[0];
        }

        return Math.max(robHelper(nums, 0, n-2), robHelper(nums, 1, n-1));

        
    }
}
