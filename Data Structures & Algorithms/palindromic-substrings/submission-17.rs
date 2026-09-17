impl Solution {
    pub fn count_substrings(s: String) -> i32 {
        fn expand(
            mut l: isize,
            mut r: isize,
            count: &mut i32,
            bytes: &[u8]
        ) {
            while l >= 0 && r < bytes.len() as isize && bytes[l as usize] == bytes[r as usize] {
                *count += 1;
                l -= 1;
                r += 1;
            }
        }

        let mut count = 0;
        let bytes = s.as_bytes();

        for i in 0..bytes.len() {
            expand(
                i as isize,
                i as isize,
                &mut count,
                bytes
            );
            expand(
                i as isize,
                i as isize+1,
                &mut count,
                bytes
            )
        }

        count as i32
    }
}
