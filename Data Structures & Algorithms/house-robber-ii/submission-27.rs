impl Solution {
    pub fn rob(nums: Vec<i32>) -> i32 {
        fn helper(nums: &[i32]) -> i32 {
            if nums.is_empty() {
                return 0;
            }

            if nums.len() == 1 {
                return nums[0];
            }

            let mut dp = vec!(0; nums.len());
            dp[0] = nums[0];
            dp[1] = max(nums[0], nums[1]);

            for i in 2..nums.len() {
                dp[i] = max(dp[i-1], nums[i] + dp[i-2]);
            }
            dp[nums.len() - 1]
        }

        if nums.len() == 1 {
            return nums[0];
        }

        max(helper(&nums[1..]), helper(&nums[..nums.len()-1]))
    }
}
