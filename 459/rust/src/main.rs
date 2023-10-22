struct Solution;

impl Solution {
    pub fn repeated_substring_pattern(s: String) -> bool {
        let n = s.len();
        for i in 1..n {
            if n % i != 0 {
                continue;
            }

            let sub = &s[..i];
            let mut res = true;
            for step in 0..(n / i) {
                if sub != &s[step * i..(step + 1) * i] {
                    res = false;
                    break;
                }
            }
            if res {
                return true;
            }
        }

        false
    }
}

fn main() {
    let s = String::from("your_input_string_here");
    let result = Solution::repeated_substring_pattern(s);
    println!("Result: {}", result);
}

