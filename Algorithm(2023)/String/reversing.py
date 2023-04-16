# 문자열 뒤집기


def reverse_two_pointer(strs: list[str]) -> list[str]:
    left, right = 0, len(strs) - 1
    while left < right:
        strs[left], strs[right] = strs[right], strs[left]
        left += 1
        right -= 1

    return strs


def reverse_list(strs: list[str]) -> list[str]:
    strs.reverse()
    return strs


def reverse_slicing(strs: list[str]) -> list[str]:
    return strs[::-1]


print(reverse_two_pointer(["h", "e", "l", "l", "o"]))
print(reverse_list(["h", "e", "l", "l", "o"]))
print(reverse_slicing(["h", "e", "l", "l", "o"]))
