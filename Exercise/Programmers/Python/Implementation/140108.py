def solution(s):
    x_idx, x_cnt, etc_cnt, answer = [0] * 4
    for i in range(len(s)):
        if s[i] == s[x_idx]:
            x_cnt += 1
        else:
            etc_cnt += 1

        if x_cnt == etc_cnt:
            answer += 1
            x_idx = i + 1

    if x_cnt != etc_cnt:
        answer += 1
    return answer


s = "banana"
print(solution(s))  # 3

s = "abracadabra"
print(solution(s))  # 6

s = "aaabbaccccabba"
print(solution(s))  # 3
