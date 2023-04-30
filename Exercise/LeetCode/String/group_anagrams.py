# 문자열 배열을 받아 애너그램 단위로 그룹핑.

"""
애너그램이란?

    일종의 언어유희로 문자를 재배열하여 다른 뜻을 가진 단어로 바꾸는 것을 말함.
    우리말 예로는, '문전박대'를 '대박전문'으로 바꿔 부르는 단어 등을 들 수 있음.

    애너그램을 판단하는 가장 간단한 방법은 정렬하여 비교하는 것.
    애너그램 관계인 단어들을 정렬하면, 서로 같은 값을 갖게 되기 때문.
"""

from collections import defaultdict
from typing import Final

words: Final[list[str]] = ["eat", "tea", "tan", "ate", "nat", "bat"]


def get_group_anagrmas_using_default_dict(strs: list[str]) -> tuple[list[str], ...]:
    anagrams = defaultdict(list)

    for word in strs:
        anagrams["".join(sorted(word))].append(word)

    return tuple(anagrams.values())


print(get_group_anagrmas_using_default_dict(words))
