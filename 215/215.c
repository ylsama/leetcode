void swap(int* x, int* y) {
    int tmp = *x;
    *x = *y;
    *y = tmp;
}

void helper(int l, int r, int* nums) {
    int target = nums[(l + r) / 2];
    int x = l;
    int y = r;
    while (x <= y) {
        while (nums[x] < target) x++;
        while (nums[y] > target) y--;
        if (x < y) {
            swap(&nums[x], &nums[y]);
            x ++;
            y --;
        }
    }
    if (l < y)
        helper(l, y, nums);
    if (x < r)
        helper(x, r, nums);
}


int findKthLargest(int* nums, int numsSize, int k){
    helper(0, numsSize-1, nums);
    for (int i=0; i<numsSize; i++) {
        printf("%d ", nums[i]);
    }
    return 0;
}

int main() {
    return 0
}
