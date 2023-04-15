# https://school.programmers.co.kr/learn/courses/30/lessons/120875

"""
문제 설명
점 네 개의 좌표를 담은 이차원 배열  dots가 다음과 같이 매개변수로 주어집니다.

[[x1, y1], [x2, y2], [x3, y3], [x4, y4]]
주어진 네 개의 점을 두 개씩 이었을 때, 두 직선이 평행이 되는 경우가 있으면 1을 없으면 0을 return 하도록 solution 함수를 완성해보세요.

제한사항
0 ≤ dots의 원소 ≤ 100
dots의 길이 = 4
dots의 원소의 길이 = 2
dots의 원소는 [x, y] 형태이며 x, y는 정수입니다.
서로 다른 두개 이상의 점이 겹치는 경우는 없습니다.
두 직선이 겹치는 경우(일치하는 경우)에도 1을 return 해주세요.
입출력 예
dots	result
[[1, 4], [9, 2], [3, 8], [10, 4]]	1
[[3, 5], [4, 1], [2, 4], [5, 10]]	0
입출력 예 설명
입출력 예 #1

점 [1, 4], [3, 8]을 잇고 [9, 2], [10, 4]를 이으면 두 선분은 평행합니다.
입출력 예 #2

점을 어떻게 연결해도 평행하지 않습니다.
"""

from itertools import combinations


def solution(dots: list[list[int]]) -> int:
    comb = list(combinations(dots, 2))
    for i in range(len(comb)):
        dot1, dot2 = comb[i]
        if dot1[0] - dot2[0] == 0:
            continue
        else:
            m1 = (dot1[1] - dot2[1]) / (dot1[0] - dot2[0])
        for j in range(i + 1, len(comb)):
            dot1, dot2 = comb[j]
            if dot1[0] - dot2[0] == 0:
                continue
            else:
                m2 = (dot1[1] - dot2[1]) / (dot1[0] - dot2[0])
            if m1 == m2:
                return 1
    return 0
