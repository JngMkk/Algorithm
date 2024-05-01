def solution(arr):
    def quad_zip(array):
        n = len(array)
        base = array[0][0]
        div = 0
        for i in range(n):
            for j in range(n):
                if array[i][j] != base:
                    div = n // 2
                    break

        if div != 0:
            quad_zip([row[:div] for row in array[:div]])
            quad_zip([row[div:] for row in array[:div]])
            quad_zip([row[:div] for row in array[div:]])
            quad_zip([row[div:] for row in array[div:]])
        else:
            answer[base] += 1

    answer = [0, 0]
    quad_zip(arr)
    return answer


def solution2(arr):
    """
    아래 위 함수 모두 옹일한 시간 복잡도를 가지고 있지만,
    이 함수는 불필요한 배열 슬라이싱을 피할 수 있기 때문에 더 효율적으로 동작함. (동일한 배열을 사용하므로 캐싱될 수 있음)
    """

    def quad_zip(n, r, c):
        base = arr[r][c]
        div = 0
        for i in range(n):
            for j in range(n):
                if arr[i + r][j + c] != base:
                    div = n // 2
                    break

        if div != 0:
            quad_zip(div, r, c)
            quad_zip(div, r + div, c)
            quad_zip(div, r, c + div)
            quad_zip(div, r + div, c + div)
            return
        answer[base] += 1

    answer = [0, 0]
    quad_zip(len(arr), 0, 0)
    return answer


arr = [[1, 1, 0, 0], [1, 0, 0, 0], [1, 0, 0, 1], [1, 1, 1, 1]]
print(solution2(arr))  # [4, 9]

arr = [
    [1, 1, 1, 1, 1, 1, 1, 1],
    [0, 1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 1, 1, 1, 1],
    [0, 1, 0, 0, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 1, 0, 0, 1],
    [0, 0, 0, 0, 1, 1, 1, 1],
]
print(solution2(arr))  # [10, 15]
