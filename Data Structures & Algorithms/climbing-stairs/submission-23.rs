impl Solution {
    pub fn climb_stairs(n: i32) -> i32 {
        match n {
            1 => return 1,
            2 => return 2,
            _ => {}
        }

        let mut two_step_back = 1;
        let mut one_step_back = 2;

        for _ in 3..=n {
            let current = one_step_back + two_step_back;
            
            two_step_back = one_step_back;
            one_step_back = current;
        }

        one_step_back
    }
}
