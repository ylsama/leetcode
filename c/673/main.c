#include <stdio.h>

int findNumberOfLIS(int *nums, int numsSize) {
  int ans = 0;
  int longest[2003] = {1}; // Initialize to 1
  int count[2003] = {1};   // Initialize to 1

  for (int i = 0; i < numsSize; i++) {
    int curr_count = 1; // Initialize the current count to 1
    for (int j = 0; j < i;
         j++) { // Use '<' instead of '<=' to avoid unnecessary checks
      if (nums[i] > nums[j]) {
        if (1 + longest[j] > longest[i + 1]) {
          curr_count = count[j];           // Update current count
          longest[i + 1] = 1 + longest[j]; // Update longest LIS ending at i
        } else if (1 + longest[j] == longest[i + 1]) {
          curr_count += count[j]; // Increment current count
        }
      }
    }
    count[i + 1] = curr_count; // Update the count for the current index
  }

  // The LIS count is the maximum LIS length (ans) in the last element of the
  // longest array
  ans = count[numsSize];
  return ans;
}

int main() {
  int nums[] = {1, 3, 3, 4, 4, 5, 5, 6, 6, 9};
  int numsSize = sizeof(nums) / sizeof(nums[0]);
  int result = findNumberOfLIS(nums, numsSize);
  printf("%d\n", result);
  return 0;
}
