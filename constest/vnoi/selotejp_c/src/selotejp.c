#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_N 1001
#define MAX_M 11

int cache[MAX_N][MAX_M][1 << MAX_M];

int helper(int i, int j, int mask, char a[MAX_N][MAX_M], int cache[MAX_N][MAX_M][1 << MAX_M]) {
    if (i == 0 && j == 0) {
        if (a[i][j] == '.') {
            return 0;
        } else {
            return 1;
        }
    }
    return cache[i][j][mask];
}

int solution(int n, int m, char a[MAX_N][MAX_M]) {
    memset(cache, 0, sizeof(cache));

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (i == 0 && j == 0) {
                continue;
            }
            int last_i = (j > 0) ? i : (i - 1);
            int last_j = (j > 0) ? (j - 1) : (m - 1);

            for (int mask = 0; mask < (1 << m); mask++) {
                int possible[4] = {
                    ((a[i][j] == '#') ? 1 : 0) + helper(last_i, last_j, mask, a, cache),
                    ((a[i][j] == '#') ? 1 : 0) + helper(last_i, last_j, mask ^ (1 << j), a, cache),
                    ((a[i][j] == '#') ? 1 : 0) + helper(last_i, last_j, mask ^ (1 << j), a, cache),
                    ((a[i][j] == '#') ? 1 : 0) + helper(last_i, last_j, mask ^ (1 << j), a, cache),
                };

                if (j > 0) {
                    if (((mask >> j) & 1) == ((mask >> (j - 1)) & 1) && ((mask >> j) & 1) == 0 && a[i][j - 1] == '#' && a[i][j] == '#') {
                        possible[2] = helper(last_i, last_j, mask, a, cache);
                        possible[3] = helper(last_i, last_j, mask ^ (1 << j), a, cache);
                    }
                }

                if (i > 0) {
                    if (((mask >> j) & 1) == 1 && a[i - 1][j] == '#' && a[i][j] == '#') {
                        possible[2] = helper(last_i, last_j, mask, a, cache);
                    }
                }

                int min_possible = possible[0];
                for (int p = 1; p < 4; p++) {
                    if (possible[p] < min_possible) {
                        min_possible = possible[p];
                    }
                }

                cache[i][j][mask] = min_possible;
            }
        }
    }

    int minvalue = cache[n - 1][m - 1][0];
    for (int mask = 0; mask < (1 << m); mask++) {
        if (minvalue > cache[n - 1][m -1][mask]) {
            minvalue = cache[n - 1][m -1][mask];
        }
    }

    return minvalue;
}

int main() {
    int n, m;
    scanf("%d %d\n", &n, &m);
    char a[MAX_N][MAX_M];

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            scanf("%c", &a[i][j]);
        }
        if (i < n-1) scanf("\n");
    }

    int out = solution(n, m, a);
    printf("%d\n", out);
    return 0;
}

