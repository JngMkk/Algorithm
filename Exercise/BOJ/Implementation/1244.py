# https://www.acmicpc.net/problem/1244

"""
입력
첫째 줄에는 스위치 개수가 주어진다. 스위치 개수는 100 이하인 양의 정수이다. 둘째 줄에는 각 스위치의 상태가 주어진다. 켜져 있으면 1, 꺼져있으면 0이라고 표시하고 사이에 빈칸이 하나씩 있다. 셋째 줄에는 학생수가 주어진다. 학생수는 100 이하인 양의 정수이다. 넷째 줄부터 마지막 줄까지 한 줄에 한 학생의 성별, 학생이 받은 수가 주어진다. 남학생은 1로, 여학생은 2로 표시하고, 학생이 받은 수는 스위치 개수 이하인 양의 정수이다. 학생의 성별과 받은 수 사이에 빈칸이 하나씩 있다.

출력
스위치의 상태를 1번 스위치에서 시작하여 마지막 스위치까지 한 줄에 20개씩 출력한다. 예를 들어 21번 스위치가 있다면 이 스위치의 상태는 둘째 줄 맨 앞에 출력한다. 켜진 스위치는 1, 꺼진 스위치는 0으로 표시하고, 스위치 상태 사이에 빈칸을 하나씩 둔다.

예제 입력 1
8
0 1 0 1 0 0 0 1
2
1 3
2 3
예제 출력 1
1 0 0 0 1 1 0 1
"""

import sys

inp = sys.stdin.readline


def man(arr: list, ind: int, num: int) -> list:
    global d

    for i in range(ind, num, ind):
        arr[i - 1] = d[arr[i - 1]]
    return arr


def woman(arr: list, ind: int, num: int) -> list:
    global d

    arr[ind] = d[arr[ind]]
    if ind == 0 or ind == num - 1:
        return arr

    i = 1
    while ind - i >= 0 and ind + i <= num - 1 and arr[ind - i] == arr[ind + i]:
        arr[ind - i], arr[ind + i] = d[arr[ind - i]], d[arr[ind + i]]
        i += 1

    return arr


n = int(inp())
switch = list(map(int, inp().split()))
d = {0: 1, 1: 0}
k = int(inp())
for _ in range(k):
    sex, num = map(int, inp().split())

    if sex == 1:
        swtich = man(switch, num, n + 1)
    else:
        switch = woman(switch, num - 1, n)

for i, s in enumerate(switch, start=1):
    print(s, end=" ")
    if not i % 20:
        print()
