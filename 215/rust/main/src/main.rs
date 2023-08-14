fn partition(nums: &mut [i32], low: usize, high: usize) -> usize {
    let pivot = nums[high];
    let mut i = low as isize - 1;

    for j in low..high {
        if nums[j] <= pivot {
            i += 1;
            nums.swap(i as usize, j);
        }
    }
    nums.swap((i + 1) as usize, high);
    (i + 1) as usize
}

fn quick_select(nums: &mut [i32], low: usize, high: usize, pos: usize) -> i32 {
    if low < high {
        let pivot_index = partition(nums, low, high);
        if pivot_index == pos {
            return nums[pivot_index];
        } else if pivot_index > pos {
            return quick_select(nums, low, pivot_index - 1, pos);
        } else {
            return quick_select(nums, pivot_index + 1, high, pos);
        }
    } else if low == pos {
        return nums[low];
    }
    -1
}

fn find_kth_largest(nums: &mut [i32], k: usize) -> i32 {
    quick_select(nums, 0, nums.len() - 1, nums.len() - k)
}

fn main() {
    let size = 5;
    let mut numbers = vec![2; size];

    numbers[0] = 12;
    numbers[1] = -12;
    numbers[2] = -2;
    numbers[3] = 122;
    numbers[4] = 2;

    let res = find_kth_largest(&mut numbers, 3);
    println!("{}", res);
}

