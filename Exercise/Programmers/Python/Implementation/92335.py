def convert(n, k):
    div, mod = divmod(n, k)
    if div == 0:
        return str(mod)
    else:
        return convert(div, k) + str(mod)


def is_prime(n):
    if n == 1:
        return False

    for i in range(2, int(n ** (1 / 2)) + 1):
        if n % i == 0:
            return False
    return True


def solution(n, k):
    cnt = 0
    for num in map(int, filter(lambda x: x, convert(n, k).split("0"))):
        if is_prime(num):
            cnt += 1
    return cnt


n = 437674
k = 3
print(solution(n, k))  # 3

n = 110011
k = 10
print(solution(n, k))  # 2
