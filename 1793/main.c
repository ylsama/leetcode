int maximumScore(int* nums, int numsSize, int k){
    int l = k;
    int r = k;
    int minElement = nums[k];
    int score = nums[k];
    int currScore = -1;
    while (l >= 0 && r < numsSize) {
        while (l > 0) {
            if (nums[l-1] >= minElement) {
                l --;
            } else {
                break;
            }
        }
        while (r < numsSize-1) {
            if (nums[r+1] >= minElement) {
                r ++;
            } else {
                break;
            }
        }

        currScore = minElement * (r - l + 1);
        if (score < currScore) {
            score = currScore;
        }

        if (l == 0 && r == numsSize -1) {
            break;
        }
        if (l == 0) {
            r ++;
            minElement = nums[r];
            continue;
        }
        if (r == numsSize - 1) {
            l --;
            minElement = nums[l];
            continue;
        }
        if (nums[l-1] > nums[r+1]) {
            l --;
            minElement = nums[l];
        } else {
            r ++;
            minElement = nums[r];
        }
    }
    
    return score;
}
