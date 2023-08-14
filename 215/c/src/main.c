#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void printNums(int *nums, int numsSize, int k) {
  for (int i = 0; i < numsSize; i++) {
    printf("%d ", nums[i]);
  }
  printf("\n");
}

void swap(int *x, int *y) {
  int tmp = *x;
  *x = *y;
  *y = tmp;
}

int partition(int *nums, int low, int high) {
  int pivot = nums[high];
  int i = (low - 1);

  for (int j = low; j <= high - 1; j++) {
    if (nums[j] <= pivot) {
      i++;
      swap(&nums[i], &nums[j]);
    }
  }
  swap(&nums[i + 1], &nums[high]);
  return (i + 1);
}

int quickSellect(int *nums, int low, int high, int pos) {
  if (low < high) {
    int pivotIndex = partition(nums, low, high);
    if (pivotIndex == pos) {
      return nums[pivotIndex];
    } else if (pivotIndex > pos) {
      return quickSellect(nums, low, pivotIndex - 1, pos);
    } else {
      return quickSellect(nums, pivotIndex + 1, high, pos);
    }
  } else if (low == pos) {
    return nums[low];
  }
  return -1;
}

void quicksort(int *nums, int low, int high) {
  if (low < high) {
    int pivotIndex = partition(nums, low, high);
    quicksort(nums, low, pivotIndex - 1);
    quicksort(nums, pivotIndex + 1, high);
  }
}

int findKthLargest(int *nums, int numsSize, int k) {
  printNums(nums, numsSize, k);
  quicksort(nums, 0, numsSize - 1);
  // return quickSellect(nums, 0, numsSize - 1, numsSize - k);
  printNums(nums, numsSize, k);
  return nums[numsSize - k];
}

int main() {
  srand(time(NULL));
  int size = 5;
  int *numbers = (int *)malloc(size * sizeof(int));

  for (int i = 0; i < size; i++) {
    numbers[i] = 2;
  }

  numbers[0] = 12;
  numbers[1] = -12;
  numbers[2] = -2;
  numbers[3] = 122;
  numbers[4] = 2;

  int res = findKthLargest(numbers, size, 3);
  printf("%d ", res);
  return 0;
}
