def solution(expression):
    from itertools import permutations

    expr_func_map = {"*": lambda x, y: x * y, "+": lambda x, y: x + y, "-": lambda x, y: x - y}
    nums = []
    operators = []
    num = ""
    for expr in expression:
        if expr.isdigit():
            num += expr
        else:
            nums.append(int(num))
            operators.append(expr)
            num = ""
    nums.append(int(num))

    unique_operator = set(operators)
    results = []
    for ordering in permutations(unique_operator, len(unique_operator)):
        nums_cp = nums[:]
        operators_cp = operators[:]
        for operator in ordering:
            func = expr_func_map[operator]

            while operator in operators_cp:
                idx = operators_cp.index(operator)
                num = func(nums_cp[idx], nums_cp[idx + 1])
                nums_cp[idx] = num
                operators_cp.pop(idx)
                nums_cp.pop(idx + 1)

        results.append(abs(nums_cp[0]))
    return max(results)


expression = "100-200*300-500+20"
print(solution(expression))  # 60420

expression = "50*6-3*2"
print(solution(expression))  # 300
