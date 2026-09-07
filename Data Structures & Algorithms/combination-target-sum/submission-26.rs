impl Solution {
    pub fn combination_sum(nums: Vec<i32>, target: i32) -> Vec<Vec<i32>> {
        fn dfs(
            start: usize,
            remaining: i32,
            candidates: &[i32],
            current: &mut Vec<i32>,
            result: &mut Vec<Vec<i32>>,
        ) {
            if remaining == 0 {
                result.push(current.clone());
                return;
            }

            for i in start..candidates.len() {
                let value = candidates[i];

                if value > remaining {
                    break;
                }

                current.push(value);

                dfs(
                    i,
                    remaining - value,
                    candidates,
                    current,
                    result
                );

                current.pop();
            }

        }

        let mut nums = nums;
        nums.sort();

        let mut result = Vec::new();
        let mut current = Vec::new();

        dfs(
            0,
            target,
            &nums,
            &mut current,
            &mut result
        );

        result
    }
}
