# 이 문제에서는 대소문자 여부를 구분하지 않음. 영문자, 숫자만을 대상으로 함.

import re
from collections import deque
from typing import Final

s: Final[str] = "A man, a plan, a canal: Panama"


def is_palindrome(string: str) -> bool:
    """list 이용하여 팰린드롬 여부 판별"""

    strs = []
    for char in string:
        if char.isalnum():
            strs.append(char.lower())
    print(strs)

    # * 판별
    while len(strs) > 1:
        if strs.pop(0) != strs.pop():
            return False
    return True


def is_palindrome2(string: str) -> bool:
    """deque을 이용하여 팰린드롬 여부 판별"""

    strs: deque[str] = deque()
    for char in string:
        if char.isalnum():
            strs.append(char.lower())
    print(strs)

    while len(strs) > 1:
        if strs.popleft() != strs.pop():
            return False
    return True


def is_palindrome3(string: str) -> bool:
    """슬라이싱을 이용하여 팰린드롬 여부 판별"""

    string = string.lower()
    # * 정규식을 이용하여 불필요한 문자 필터링
    string = re.sub("[^a-z0-9]", "", string)
    print(string)

    return string == string[::-1]


print(is_palindrome(s))
print(is_palindrome2(s))
print(is_palindrome3(s))

"""
실행 시간 비교: list > deque > slicing

list의 pop(0): O(n)
deque의 popleft(): O(1)

각각 n번씩 반복하면, list는 O(n^2), deque는 O(n)

슬라이싱은 CPython을 이용하므로 좋은 속도를 기대할 수 있음.
"""
