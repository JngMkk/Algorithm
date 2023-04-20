"""
    기준 데이터를 설정하고 그 기준보다 큰 데이터와 작은 데이터의 위치를 바꾸는 방법.

    일반적인 상황에서 가장 많이 사용되는 정렬 알고리즘 중 하나.

    병합 정렬과 더불어 대부분의 프로그래밍 언어의 정렬 라이브러리의 근간이 되는 알고리즘.

    가장 기본적인 퀵 정렬은 첫 번째 데이터를 기준 데이터를 설정함.

    평균의 경우 O(NlogN)의 시간 복잡도를 가짐

    최악의 경우 O(N^2)의 시간 복잡도를 가짐
"""


# 첫 번째 방법
def quick_sort(array, start, end):
    # 원소의 개수가 1인 경우
    if start >= end:
        return

    pivot = start
    left = start + 1
    right = end

    while left <= right:
        while left <= end and array[left] <= array[pivot]:
            left += 1

        while right > start and array[right] >= array[pivot]:
            right -= 1

        # 엇갈렸다면 작은 데이터와 피벗을 교체
        if left > right:
            array[right], array[pivot] = array[pivot], array[right]

        else:
            array[left], array[right] = array[right], array[left]

    quick_sort(array, start, right - 1)
    quick_sort(array, right + 1, end)


# 두 번째 방법
def quick_sort2(array):
    if len(array) <= 1:
        return array
    pivot = array[0]
    tail = array[1:]

    left_side = [x for x in tail if x <= pivot]
    right_side = [x for x in tail if x > pivot]

    return quick_sort2(left_side) + [pivot] + quick_sort2(right_side)


arr = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
quick_sort(arr, 0, len(arr) - 1)
print(arr)
