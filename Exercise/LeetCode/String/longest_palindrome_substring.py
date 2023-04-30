# 가장 긴 팰린드롬 부분 문자열 추출
from typing import Final

s1: Final[str] = "babad"
# * response: "bab" or "aba"

s2: Final[str] = "cbbd"
# * response: "bb"


# * 풀이 1: 중앙을 중심으로 확장하는 풀이 (two pointer)
def longest_palindrome_using_two_pointer(word: str) -> str:
    def expand(left: int, right: int) -> str:
        while left >= 0 and right < len(word) and word[left] == word[right]:
            left -= 1
            right += 1
        return word[left + 1 : right]

    # * 해당 사항이 없을 때 리턴
    if len(word) < 2 or word == word[::-1]:
        return word

    res = ""
    # * 슬라이딩 윈도우 우측으로 이동
    for i in range(len(word) - 1):
        res = max(res, expand(i, i + 1), expand(i, i + 2), key=len)

    return res


print(longest_palindrome_using_two_pointer(s1))
print(longest_palindrome_using_two_pointer(s2))
