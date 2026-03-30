class Solution {
    public int maxProduct(int[] nums) {
        int n = nums.length;
        int maxProd = nums[0];
        int minProd = nums[0];
        int globalMax = nums[0];

        for (int i = 1; i < n; i++) {
            int tempMax = maxProd;
            maxProd = Math.max(Math.max(nums[i], nums[i] * maxProd), nums[i] * minProd);
            minProd = Math.min(Math.min(nums[i], nums[i] * tempMax), nums[i] * minProd);
            globalMax = Math.max(globalMax, maxProd);
        }

        return globalMax;
    }
}