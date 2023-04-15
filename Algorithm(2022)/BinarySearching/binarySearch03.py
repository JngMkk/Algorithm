"""
    문제

        N개의 원소를 포함하고 있는 수열이 오름차순으로 정렬되어 있음. 이때 이 수열에서 x가 등장하는 횟수를 계산.
        예를 들어 수열 {1, 1, 2, 2, 2, 2, 3}이 있을 때 x = 2라면, 현재 수열에서 값이 2인 원소가 4개이므로 4를 출력함

        단, 이 문제는 시간 복잡도 O(logN)으로 알고리즘을 설계하지 않으면 시간 초과 판정을 받음.

        첫째 줄에 N가 x가 정수 형태로 공백으로 구분되어 입력 (1 <= N <= 1,000,000), (-10^9 <= x <= 10^9)

        둘째 줄에 N개의 원소가 정수 형태로 공백으로 구분되어 입력됨. (-10^9 <= 각 원소의 값 <= 10^9)

        수열의 원소 중에서 값이 x인 원소의 개수를 출력함. 단, 값이 x인 원소가 하나도 없다면 -1을 출력.
"""

# 나의 풀이
n, x = map(int, input().split())
arr = list(map(int, input().split()))


def left_idx(array, target, start, end):
    while start < end:
        mid = (start + end) // 2
        if array[mid] < target:
            start = mid + 1
        else:
            end = mid
    return start


def right_idx(array, target, start, end):
    while start < end:
        mid = (start + end) // 2
        if array[mid] > target:
            end = mid
        else:
            start = mid + 1
    return start


cnt = right_idx(arr, x, 0, len(arr)) - left_idx(arr, x, 0, len(arr))
if cnt == 0:
    print(-1)
else:
    print(cnt)

"""
    문제 해결 아이디어

        시간 복잡도 O(logN)으로 동작하는 알고리즘을 요구하고 있음.
            - 일반적인 선형 탐색으로는 시간 초과 판정을 받음
            - 하지만 데이터가 정렬되어 있기 때문에 이진 탐색을 수행할 수 있음.

        특정 값이 등장하는 첫 번째 위치와 마지막 위치를 찾아 위치 차이를 계산해 문제를 해결할 수 있음.
"""
