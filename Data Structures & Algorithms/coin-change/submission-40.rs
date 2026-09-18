impl Solution {
    pub fn coin_change(coins: Vec<i32>, amount: i32) -> i32 {
        let mut coins = coins;
        coins.sort();
        let amount = amount as usize;

        let mut dp = vec![amount as i32 + 1; amount + 1];
        dp[0] = 0;

        for i in 1..=amount {
            for &c in &coins {
                let coin = c as usize;
                if coin > i {
                    break;
                }

                dp[i] = dp[i].min(dp[i - coin] + 1);
            }
        }

        if dp[amount] == amount as i32 + 1 {
            -1
        } else {
            dp[amount]
        }
    }
}
