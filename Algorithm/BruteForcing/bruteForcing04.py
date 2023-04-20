"""
    문제

        알파벳 대문자와 숫자(0~9)로만 구성된 문자열이 입력으로 주어짐.
        이때 모든 알파벳을 오름차순으로 정렬하여 이어서 출력한 뒤에, 그 뒤에 모든 숫자를 더한 값을 이어서 출력함.

        예를 들어 K1KA5CB7이라는 값이 들어오면 ABCKK13을 출력함
"""

# 나의 풀이
_str = input()
al = []
num = []
res = ""

for s in _str:
    if s.isalpha():
        al.append(s)
    elif s.isdigit():
        num.append(int(s))

for a in sorted(al):
    res += a

print(res + str(sum(num)))


"""
    문제 해결 아이디어

        요구사항대로 충실히 구현하면 되는 문제임.
        문자열이 입력되었을 때 문자를 하나씩 확인함.
            - 숫자인 경우 따로 합계를 계산함
            - 알바벳의 경우 별도의 리스트에 저장
        결과적으로 리스트에 저장된 알파벳을 정렬해 출력하고, 합계를 뒤에 붙여 출력하면 됨.
"""

# 해답
_str = input()
res = 0
al = []

for s in _str:
    if s.isalpha():
        al.append(s)
    else:
        res += int(s)

al.sort()

# 숫자가 0으로 들어올 수도 있지 않나....?
if res != 0:
    al.append(str(res))

print("".join(al))
