def solution(triangle):
    n = len(triangle)
    for i in range(1, n):
        for j in range(i + 1):
            left = 0 if j - 1 < 0 else triangle[i - 1][j - 1]
            right = 0 if j == i else triangle[i - 1][j]
            triangle[i][j] = triangle[i][j] + max(left, right)
    return max(triangle[n - 1])


triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
print(solution(triangle))  # 30
