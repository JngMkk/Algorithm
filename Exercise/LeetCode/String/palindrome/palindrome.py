"""
주어진 문자열이 팰린드롬인지 확인.
대소문자를 구분하지 않으며, 영문자와 숫자만을 대상으로 함.

https://leetcode.com/problems/valid-palindrome
"""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        """Runtime: 36ms / Memory: 18MB"""

        import re

        s = s.lower()
        s = re.sub(r"[^0-9a-z]", "", s)

        return s == s[::-1]

    def isPalindrome2(self, s: str) -> bool:
        """Runtime: 52ms / Memory: 17.1MB"""

        s = s.lower()
        cleaned_s = ""

        for char in s:
            if char.isalnum():
                cleaned_s += char

        left, right = 0, len(cleaned_s) - 1
        while left <= right:
            if cleaned_s[left] != cleaned_s[right]:
                return False
            left += 1
            right -= 1

        return True

    def isPalindrome3(self, s: str) -> bool:
        """Runtime: 234ms / Memory: 21.8MB"""

        strs = []
        for char in s:
            if char.isalnum():
                strs.append(char.lower())

        while len(strs) > 1:
            if strs.pop(0) != strs.pop():
                return False

        return True

    def isPalindrome4(self, s: str) -> bool:
        """
        Runtime: 52ms / Memory: 17.2MB

        deque: 양방향 queue (double-ended queue)

        popleft(): O(1)
        appendleft(): O(1)

        maxlen을 지정하고 가득 찬 경우, 반대편에 있는 원소가 삭제되고 최대 크기 유지.
        양방향에서 thread-safe.
        """

        from collections import deque

        _deque: deque = deque()
        s = s.lower()
        for char in s:
            if char.isalnum():
                _deque.append(char)

        while len(_deque) > 1:
            if _deque.popleft() != _deque.pop():
                return False

        return True
