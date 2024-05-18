def solution(gems):
    gem_types = set(gems)
    n_gem_types = len(gem_types)
    counter = {k: 0 for k in gem_types}

    start, curr_types_cnt, min_interval = 0, 0, 100001
    answer = [1, 1]
    for end, gem in enumerate(gems):
        if counter[gem] == 0:
            curr_types_cnt += 1
        counter[gem] += 1

        while curr_types_cnt == n_gem_types:
            _gem = gems[start]
            counter[gems[start]] -= 1
            if counter[_gem] == 0:
                curr_types_cnt -= 1
                if (interval := end - start) < min_interval:
                    answer = [start + 1, end + 1]
                    min_interval = interval
            start += 1

    return answer


gems = ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]
print(solution(gems))  # [3, 7]

gems = ["AA", "AB", "AC", "AA", "AC"]
print(solution(gems))  # [1, 3]

gems = ["XYZ", "XYZ", "XYZ"]
print(solution(gems))  # [1, 1]

gems = ["ZZZ", "YYY", "NNNN", "YYY", "BBB"]
print(solution(gems))  # [1, 5]
