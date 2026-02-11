#include <iostream>
#include <vector>

std::vector<long long> dp;

// bottom-up
int main() {
    int n = 50;
    dp.assign(n + 1, 0);
    dp[1] = 1;
    dp[2] = 1;

    for (int i = 3; i <= n; ++i) {
        dp[i] = dp[i - 1] + dp[i - 2];
    }

    std::cout << dp[n] << "\n";

    return 0;
}