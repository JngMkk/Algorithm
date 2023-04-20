# 로그 파일 재정렬

"""
재정렬 기준
    1. 로그의 가장 앞 부분은 식별자.
    2. 문자로 구성된 로그가 숫자 로그보다 앞에 옴.
    3. 식별자는 순서에 영향을 끼치지 않지만, 문자가 동일할 경우 식별자 순으로 함.
    4. 숫자 로그는 입력 순서대로 함.
"""

_logs = ["dig1 8 1 5", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]


def func(x: str) -> tuple[list[str], str]:
    splited = x.split()
    return splited[1:], splited[0]


def reorder_with_lambda(logs: list[str]) -> list[str]:
    letters: list[str] = []
    digits: list[str] = []

    for log in logs:
        if log.split()[1].isdigit():
            digits.append(log)
        else:
            letters.append(log)

    # * 식별자를 제외한 문자열을 키로 정렬, 후순위로 식별자
    letters.sort(key=func)
    return letters + digits


print(reorder_with_lambda(_logs))
