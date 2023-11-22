def solution(id_list: list[str], report: list[str], k: int) -> list[int]:
    def new_report_dic():
        return {_id: [set(), set()] for _id in id_list}

    report_dic = new_report_dic()
    for rep in report:
        rep_from, rep_to = rep.split()
        report_dic[rep_from][1].add(rep_to)
        report_dic[rep_to][0].add(rep_from)

    answer = []
    for data in report_dic.values():
        cnt = 0
        for _id in data[1]:
            if len(report_dic[_id][0]) >= k:
                cnt += 1
        answer.append(cnt)

    return answer


id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"]
k = 2
print(solution(id_list, report, k))  # [2,1,1,0]

id_list = ["con", "ryan"]
report = ["ryan con", "ryan con", "ryan con", "ryan con"]
k = 3
print(solution(id_list, report, k))  # [0,0]
