impl Solution {
    pub fn rob(nums: Vec<i32>) -> i32 {

        if nums.is_empty() {
            return 0;
        }

        if nums.len() == 1 {
            return nums[0];
        }

        if nums.len() == 2 {
            return max(nums[0], nums[1]);
        }

        let mut count = vec![0; nums.len()];

        count[0] = nums[0];
        count[1] = max(nums[0], nums[1]);

        for i in 2..nums.len() {
            count[i] = max(count[i-2] + nums[i], count[i-1]);
        }

        count[nums.len() - 1]
    }
}
