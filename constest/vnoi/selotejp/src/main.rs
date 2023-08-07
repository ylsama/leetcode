use std::io;

fn helper(i: usize, j: usize, mask: usize, a: &Vec<String>, cache: &Vec<Vec<Vec<i32>>>) -> i32 {
    if i == 0 && j == 0 {
        if &a[i][j..=j] == "." {
            return 0;
        } else {
            return 1;
        }
    }
    cache[i][j][mask]
}

fn solution(n: usize, m: usize, a: &Vec<String>) -> i32 {
    let mut cache = vec![vec![vec![0; 1 << m]; m]; n];
    for i in 0..n {
        for j in 0..m {
            if i == 0 && j == 0 {
                continue;
            }
            let last: (usize, usize) = if j > 0 { (i, j - 1) } else { (i - 1, m - 1) };
            for mask in 0..(1 << m) {
                let mut possible = vec![];
                possible.push(
                    if &a[i][j..=j] == "#" { 1 } else { 0 }
                        + helper(last.0, last.1, mask, &a, &cache),
                );
                possible.push(
                    if &a[i][j..=j] == "#" { 1 } else { 0 }
                        + helper(last.0, last.1, mask ^ (1 << j), &a, &cache),
                );

                if j > 0
                    && (mask >> j) & 1 == (mask >> (j - 1)) & 1
                    && (mask >> j) & 1 == 0
                    && &a[i][j - 1..=j] == "##"
                {
                    possible.push(helper(last.0, last.1, mask, &a, &cache));
                    possible.push(helper(last.0, last.1, mask ^ (1 << j), &a, &cache));
                }

                if i > 0 && (mask >> j) & 1 == 1 && &a[i - 1][j..=j] == "#" && &a[i][j..=j] == "#" {
                    possible.push(helper(last.0, last.1, mask, &a, &cache));
                }

                cache[i][j][mask] = *possible.iter().min().unwrap();
            }
        }
    }

    *cache[n - 1][m - 1].iter().min().unwrap()
}

fn main() {
    let mut input = String::new();
    io::stdin()
        .read_line(&mut input)
        .expect("Failed to read line");
    let mut parts = input.trim().split_whitespace();
    let n: usize = parts
        .next()
        .expect("Invalid input")
        .parse()
        .expect("Invalid input");
    let m: usize = parts
        .next()
        .expect("Invalid input")
        .parse()
        .expect("Invalid input");

    let mut a = Vec::new();
    for _ in 0..n {
        let mut row = String::new();
        io::stdin()
            .read_line(&mut row)
            .expect("Failed to read line");
        a.push(row.trim().to_string());
    }
    println!("{}", solution(n, m, &a));
}
