# 덧셈하여 타겟을 만들 수 있는 배열의 두 숫자 인덱스를 리턴
from typing import Optional

arr = [2, 7, 11, 15]
target = 9


def brute_force(nums: list[int], target: int) -> Optional[list[int]]:
    """시간 복잡도 O(n^2)"""

    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return None


def using_in(nums: list[int], target: int) -> Optional[list[int]]:
    """
    시간 복잡도 O(n^2)

    같은 시간 복잡도라도 in 연산이 훨씬 빠르고 가벼움.
    """
    for i, num in enumerate(nums):
        complement = target - num

        # * in의 시간 복잡도 O(n)
        if complement in nums[i + 1 :]:
            return [nums.index(num), nums[i + 1 :].index(complement) + (i + 1)]

    return None


def using_dict(nums: list[int], target: int) -> Optional[list[int]]:
    """시간 복잡도 O(n)"""

    # * 키와 값을 바꿔서 딕셔너리로
    nums_map: dict[int, int] = {}
    for i, num in enumerate(nums):
        if target - num in nums_map:
            return [nums_map[target - num], i]
        nums_map[num] = i

    return None


print(brute_force(arr, target))
print(using_in(arr, target))
print(using_dict(arr, target))
