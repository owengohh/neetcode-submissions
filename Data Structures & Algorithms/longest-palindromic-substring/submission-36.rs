impl Solution {
    pub fn longest_palindrome(s: String) -> String {
        fn expand(
            mut l: isize,
            mut r: isize,
            start: &mut usize,
            max_length: &mut usize,
            bytes: &[u8]
        ) {
            while l >= 0 && r < bytes.len() as isize && bytes[l as usize] == bytes[r as usize]  {

                let length = (r - l + 1) as usize;
                if length > *max_length {
                    *max_length = length;
                    *start = l as usize;
                }
                l -= 1;
                r += 1;
            }
        }

        let bytes = s.as_bytes();
        let mut idx = 0;
        let mut max_length = 0;

        for i in 0..s.len() {
            expand(i as isize, i as isize, &mut idx, &mut max_length, bytes);
            expand(i as isize, i as isize +1, &mut idx, &mut max_length, bytes);
        }

        s[idx..idx+max_length].to_string()
    }
}
