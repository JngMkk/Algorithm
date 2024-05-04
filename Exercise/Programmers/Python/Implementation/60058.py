def solution(p):
    def __check(string):
        cnt = 0
        for char in string:
            if char == "(":
                cnt += 1
            else:
                cnt -= 1
                if cnt < 0:
                    return False
        return True

    def __split():
        cnt1, cnt2 = 0, 0
        idx = 0
        while True:
            if p[idx] == "(":
                cnt1 += 1
            else:
                cnt2 += 1
            idx += 1
            if cnt1 == cnt2:
                break
        return p[:idx], p[idx:]

    if not p:
        return p

    u, v = __split()
    if __check(u):
        return u + solution(v)

    _reversed = "".join(map(lambda x: "(" if x == ")" else ")", u[1 : len(u) - 1]))
    return "(" + solution(v) + ")" + _reversed


p = "(()())()"
print(solution(p))  # "(()())()"
p = ")("
print(solution(p))  # "()"
p = "()))((()"
print(solution(p))  # "()(())()"
