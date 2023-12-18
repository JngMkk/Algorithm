def solution(info: list[str], queries: list[str]) -> list[int]:
    from bisect import bisect_left
    from collections import defaultdict

    cache = {}
    dic = defaultdict(list)
    for inf in info:
        lang, job, career, food, score = inf.split()
        score = int(score)
        for lan in ["-", lang]:
            for jo in ["-", job]:
                for car in ["-", career]:
                    for foo in ["-", food]:
                        dic[(lan, jo, car, foo)].append(score)

    for key in dic.keys():
        dic[key].sort()

    ret = []
    for query in queries:
        lang, job, career, food_score = map(lambda x: x.strip(), query.split("and"))
        food, score = food_score.split()

        scores = dic[(lang, job, career, food)]
        q = (lang, job, career, food, int(score))
        if q in cache:
            bisected_idx = cache[q]
        else:
            bisected_idx = bisect_left(scores, int(score))
            cache[q] = bisected_idx

        ret.append(len(scores) - bisected_idx)

    return ret


info = [
    "java backend junior pizza 150",
    "python frontend senior chicken 210",
    "python frontend senior chicken 150",
    "cpp backend senior pizza 260",
    "java backend junior chicken 80",
    "python backend senior chicken 50",
]
queries = [
    "java and backend and junior and pizza 100",
    "python and frontend and senior and chicken 200",
    "cpp and - and senior and pizza 250",
    "- and backend and senior and - 150",
    "- and - and - and chicken 100",
    "- and - and - and - 150",
]
print(solution(info, queries))
