def solution(today: str, terms: list[str], privacies: list[str]) -> list[int]:
    def count_days(yyyymmdd: str) -> int:
        y, m, d = map(int, yyyymmdd.split("."))
        return y * 12 * 28 + m * 28 + d

    def is_term_expired(privacy: str) -> bool:
        _date, term = privacy.split()
        duration_days_cnt = terms_dic[term]
        expire_days_cnt = count_days(_date)
        if (duration_days_cnt + expire_days_cnt) <= today_days_cnt:
            return True
        return False

    answer = []
    terms_dic = {term[0]: int(term[2:]) * 28 for term in terms}
    today_days_cnt = count_days(today)

    for idx, privacy in enumerate(privacies, 1):
        if is_term_expired(privacy):
            answer.append(idx)

    return answer


today = "2022.05.19"
terms = ["A 6", "B 12", "C 3"]
privacies = ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]
print(solution(today, terms, privacies))  # [1, 3]

today = "2020.01.01"
terms = ["Z 3", "D 5"]
privacies = ["2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"]
print(solution(today, terms, privacies))  # [1, 4, 5]
