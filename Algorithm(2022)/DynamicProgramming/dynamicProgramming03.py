"""
    문제

        정수 X가 주어졌을 때, 정수 X에 사용할 수 있는 연산은 다음과 같이 4가지
            - X가 5로 나누어 떨어지면, 5로 나눔
            - X가 3으로 나누어 떨어지면, 3으로 나눔
            - X가 2로 나누어 떨어지면, 2로 나눔
            - X에서 1을 뺌

        정수 X가 주어졌을 때, 연산 4개를 적절히 사용해서 값을 1로 만들고자 함.
        연산을 사용하는 횟수의 최솟값을 출력.

        예를 들어 정수가 26이면 다음과 같이 계산해서 3번의 연산이 최솟값.
            - 26 -> 25 -> 5 -> 1
"""

x = int(input())
d = [0] * (x + 1)

# d[1]은 항상 0이므로 d[1]은 계산할 필요 없음.
for i in range(2, x + 1):
    d[i] = d[i - 1] + 1

    if i % 2 == 0:
        d[i] = min(d[i], d[i // 2] + 1)

    if i % 3 == 0:
        d[i] = min(d[i], d[i // 3] + 1)

    if i % 5 == 0:
        d[i] = min(d[i], d[i // 5] + 1)

print(d[x])
