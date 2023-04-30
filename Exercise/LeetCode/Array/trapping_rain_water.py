# 높이를 입력받아 비 온 후 얼마나 많은 물이 쌓일 수 있는지 계산
from typing import Final

arr: Final[list[int]] = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]


def using_two_pointer(array: list[int]) -> int:
    """시간 복잡도 O(n)"""
    if not array:
        return 0

    volume = 0
    left, right = 0, len(array) - 1
    left_max, right_max = array[left], array[right]

    while left < right:
        left_max, right_max = max(array[left], left_max), max(array[right], right_max)

        if left_max <= right_max:
            volume += left_max - array[left]
            left += 1
        else:
            volume += right_max - array[right]
            right -= 1

    return volume


def using_stack(array: list[int]) -> int:
    """시간 복잡도 O(n)"""
    stack: list[int] = []
    volume = 0

    for i in range(len(array)):
        while stack and array[i] > array[stack[-1]]:
            top = stack.pop()

            if not stack:
                break

            distance = i - stack[-1] - 1
            waters = min(array[i], array[stack[-1]]) - array[top]

            volume += distance * waters

        stack.append(i)

    return volume


print(using_two_pointer(arr))
print(using_stack(arr))
