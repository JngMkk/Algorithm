def solution(n, k):
    def __factorial(n):
        if fac_map[n]:
            return fac_map[n]
        res = n * __factorial(n - 1)
        fac_map[n] = res
        return res

    def __get_order(num1, num2):
        if num2 < 0:
            return answer
        div, mod = divmod(num1, __factorial(num2))
        answer.append(people.pop(div))
        return __get_order(mod, num2 - 1)

    fac_map = [0] * n
    fac_map[0] = 1
    fac_map[1] = 1

    answer = []
    people = [i for i in range(1, n + 1)]
    return __get_order(k - 1, n - 1)


n = 3
k = 5
print(solution(n, k))  # [3,1,2]

n = 5
k = 7
print(solution(n, k))  # [1,3,2,4,5]
