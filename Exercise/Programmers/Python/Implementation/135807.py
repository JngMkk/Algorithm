def solution(arrayA, arrayB):
    def gcd(a, b):
        if a % b == 0:
            return b
        return gcd(b, a % b)

    def check_array(_gcd, array):
        if _gcd != 1:
            flag = 1
            for elem in array:
                if elem >= _gcd and elem % _gcd == 0:
                    flag = 0
                    break
            if flag:
                return _gcd
        return 0

    n = len(arrayA)
    gcd_a = arrayA[0]
    gcd_b = arrayB[0]
    for i in range(1, n):
        gcd_a = gcd(gcd_a, arrayA[i])
        gcd_b = gcd(gcd_b, arrayB[i])

    return max(check_array(gcd_a, arrayB), check_array(gcd_b, arrayA))


arrayA = [10, 17]
arrayB = [5, 20]
print(solution(arrayA, arrayB))  # 0

arrayA = [10, 20]
arrayB = [5, 17]
print(solution(arrayA, arrayB))  # 10

arrayA = [14, 35, 119]
arrayB = [18, 30, 102]
print(solution(arrayA, arrayB))  # 7
