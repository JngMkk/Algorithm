# 금지된 단어를 제외한 가장 흔하게 등장하는 단어 출력
# 대소문자 구분 x, 구두점 무시
import re
from collections import Counter, defaultdict
from typing import Final

paragraph: Final[str] = "Bob hit a ball, the hit BALL flew far after it was hit."
banned: Final[list[str]] = ["hit"]


def get_most_common_word_using_default_dict(sentence: str, ban: list[str]) -> str:
    """정규식, defaultdict 사용"""

    # * \w: 단어 문자(Word Character를 뜻하며, ^은 not을 의미함.
    # * 단어 문자가 아닌 모든 문자를 공백으로 치환한다.
    substituted = re.sub(r"[^\w]", " ", sentence).lower().split()
    words = []
    for word in substituted:
        if word not in ban:
            words.append(word)

    counts: defaultdict[str, int] = defaultdict(int)
    for word in words:
        counts[word] += 1

    # * counts에서 값이 가장 큰 key를 가져온다.
    return max(
        counts,
        key=counts.get,  # type:ignore
        # expected "Callable[[str], Union[SupportsDunderLT[Any], SupportsDunderGT[Any]]]
    )


def get_most_common_word_using_counter(sentence: str, ban: list[str]) -> str:
    """정규식, counter 사용"""

    words = [
        word
        for word in re.sub(r"[^\w]", " ", sentence).lower().split()
        if word not in ban
    ]

    counts = Counter(words)  # Counter({'ball': 2, 'bob': 1, 'a': 1, 'the': 1, ...})
    most_common = counts.most_common(1)  # [('ball', 2)]
    return most_common[0][0]


print(get_most_common_word_using_default_dict(paragraph, banned))
print(get_most_common_word_using_counter(paragraph, banned))
