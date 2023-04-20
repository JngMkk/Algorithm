"""
    순차 탐색 : 리스트 안에 있는 특정한 데이터를 찾기 위해 앞에서부터 데이터를 하나씩 확인하는 방법
    이진 탐색 : 정렬되어 있는 리스트에서 탐색 범위를 절반씩 좁혀가며 데이터를 탐색하는 방법
        - 이진 탐색은 시작점, 끝점, 중간점을 이용하여 탐색 범위를 설정함.

    시간 복잡도
        - 단계마다 탐색 범위를 2로 나누는 것과 동일하므로 연산 횟수는 log_2N에 비례함

        - 예를 들어 초기 데이터 개수가 32개일 때, 이상적으로 1단계를 거치면 16개 가량의 데이터만 남음.

        - 다시 말해 이진 탐색은 탐색 범위를 절반씩 줄이며, 시간 복잡도는 O(logN)을 보장함.
"""


# 재귀적 구현
def binary_search(array, target, start, end):
    if start > end:
        return None

    mid = (start + end) // 2

    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)
    else:
        return binary_search(array, target, mid + 1, end)


# 반복문 구현
def binary_search2(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None


n, target = list(map, input().split())
array = list(map(int, input().split()))

res = binary_search(array, target, 0, n - 1)
if res == None:
    print("원소가 존재하지 않습니다")
else:
    print(res + 1)

res = binary_search2(array, target, 0, n - 1)
if res == None:
    print("원소가 존재하지 않습니다")
else:
    print(res + 1)
