# https://school.programmers.co.kr/learn/courses/30/lessons/17681

from typing import List


def solution(n: int, arr1: List[int], arr2: List[int]) -> List[str]:
    res: List[str] = []

    for i in range(n):
        x = bin(arr1[i])[2:].zfill(n)
        y = bin(arr2[i])[2:].zfill(n)
        tmp: str = ""
        for j in range(n):
            if x[j] == "0" and y[j] == "0":
                tmp += " "
                continue
            tmp += "#"
        res.append(tmp)

    return res


# =========================================================================


def solution(n: int, arr1: List[int], arr2: List[int]) -> List[str]:
    res: List[str] = []

    for a1, a2 in zip(arr1, arr2):
        a12: str = bin(a1 | a2)[2:].zfill(n).replace("1", "#").replace("0", " ")
        res.append(a12)

    return res
