def solution(X, Y):
    from collections import Counter

    couple = Counter(X) & Counter(Y)
    if not couple:
        return "-1"

    _sorted = sorted(couple.items(), key=lambda x: -int(x[0]))
    if _sorted[0][0] == "0":
        return "0"

    return "".join(map(lambda x: x[0] * x[1], _sorted))


X = "100"
Y = "2345"
print(solution(X, Y))  # "-1"

X = "100"
Y = "203045"
print(solution(X, Y))  # "0"

X = "100"
Y = "123450"
print(solution(X, Y))  # "10"

X = "12321"
Y = "42531"
print(solution(X, Y))  # "321"

X = "5525"
Y = "1255"
print(solution(X, Y))  # "552"
