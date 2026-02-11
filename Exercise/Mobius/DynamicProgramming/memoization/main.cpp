#include <iostream>
#include <vector>

std::vector<long long> memo;

// top-down 방식
long long fibo(int n) {
    if (memo[n] != -1) return memo[n];

    if (n <= 2)
        memo[n] = 1;
    else
        memo[n] = fibo(n - 1) + fibo(n - 2);
    
    return memo[n];
}

int main() {
    int n = 50;
    memo.assign(n + 1, -1);

    std::cout << fibo(n) << "\n";

    return 0;
}