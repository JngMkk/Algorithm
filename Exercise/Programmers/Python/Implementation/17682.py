def solution(dartResult):
    scores = []
    options = {"S": 1, "D": 2, "T": 3}
    last_option_idx = -1

    for i, dart in enumerate(dartResult):
        if not dart.isdigit():
            if dart in options:
                scores.append(int(dartResult[last_option_idx + 1 : i]) ** options[dart])
            elif dart == "*":
                scores[-2:] = [x * 2 for x in scores[-2:]]
            elif dart == "#":
                scores[-1] *= -1

            last_option_idx = i

    return sum(scores)


dartResult = "1S2D*3T"  # 37
print(solution(dartResult))

dartResult = "1D2S#10S"  # 9
print(solution(dartResult))

dartResult = "1D2S0T"  # 3
print(solution(dartResult))

dartResult = "1S*2T*3S"  # 23
print(solution(dartResult))

dartResult = "1D#2S*3S"  # 5
print(solution(dartResult))

dartResult = "1T2D3D#"  # -4
print(solution(dartResult))

dartResult = "1D2S3T*"  # 59
print(solution(dartResult))
