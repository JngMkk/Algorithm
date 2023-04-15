# https://school.programmers.co.kr/learn/courses/30/lessons/49994

from typing import List, Dict, Set


def solution(dirs: str) -> int:
    direc: Dict[str, List[int]] = {"U": [0, 1], "D": [0, -1], "L": [-1, 0], "R": [1, 0]}
    direction: Set[int] = set()
    x: int = 0
    y: int = 0

    for d in dirs:
        nx: int = x + direc[d][0]
        ny: int = y + direc[d][1]
        if nx > 5 or nx < -5 or ny > 5 or ny < -5:
            continue
        direction.add((x, y, nx, ny))
        direction.add((nx, ny, x, y))
        x, y = nx, ny

    return len(direction) // 2
