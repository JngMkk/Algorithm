"""
    파이썬 이진 탐색 라이브러리

    bisect_left(a, x): 정렬된 순서를 유지하면서 배열 a에 x를 삽입할 가장 왼쪽 인덱스 반환
    bisect_right(a, x): 정렬된 순서를 유지하면서 배열 a에 x를 삽입할 가장 오른쪽 인덱스 반환
"""

# 값이 특정 범위에 속하는 데이터 개수 구하기
from bisect import bisect_left, bisect_right


def count_by_range(array, left_value, right_value):
    left_index = bisect_left(array, left_value)
    right_index = bisect_right(array, right_value)
    return right_index - left_index


a = [1, 2, 3, 3, 3, 3, 4, 4, 8, 9]

print(count_by_range(a, 4, 4))
print(count_by_range(a, -1, 3))
