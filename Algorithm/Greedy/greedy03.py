"""
    문제

        각 자리가 숫자(0~9)로만 이루어진 문자열 S가 주어졌을 때,
        왼쪽부터 오른쪽으로 하나씩 모든 숫자를 확인하며 숫자 사이에
        'x' 혹은 '+' 연산자를 넣어 결과적으로 만들어질 수 있는 가장 큰 수를 구하는 프로그램을 작성.
        단, +보다 x를 먼저 계산하는 일반적인 방식과는 달리, 모든 연산은 왼쪽부터 순서대로 이루어진다고 가정함.

        예를 들어 02984라는 문자열로 만들 수 있는 가장 큰 수는 ((((0 + 2) x 9) x 8) x 4) = 576임
        또한 만들어질 수 있는 가장 큰 수는 항상 20억 이하의 정수가 되도록 입력이 주어짐.
"""

# 나의 풀이
s = input()
res = int(s[0])

for i in range(0, len(s) - 1):
    if res < 2 or int(s[i + 1]) < 2:
        res += int(s[i + 1])
    else:
        res *= int(s[i + 1])

print(res)

"""
    문제 해결 아이디어

        대부분의 경우 +보다는 x가 더 값을 크게 만듦.
        다만 두 수 중에서 하나라도 '0' 혹은 '1'인 경우, 곱하기보다는 더하기를 수행하는 것이 효율적임.
        따라서 두 수에 대하여 연산을 수행할 때, 두 수 중에서 하나라도 1 이하인 경우에는 더하며,
        두 수가 모두 2 이상인 경우에는 곱하면 정답임.
"""

# 해답
s = input()
res = int(s[0])

for i in range(1, len(s)):
    n = int(s[i])
    if n < 2 or res < 2:
        res += n
    else:
        res *= n

print(res)
