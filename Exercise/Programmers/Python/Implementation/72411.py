def solution(orders: list[str], course: list[int]) -> list[str]:
    from collections import Counter
    from itertools import combinations

    course_menus = []
    for r in course:
        r_course_menus = []
        for order in orders:
            for comb in combinations(sorted(order), r):
                course_menu = "".join(comb)
                r_course_menus.append(course_menu)

        if not r_course_menus:
            continue

        ordered_by_cnt_desc = Counter(r_course_menus).most_common()
        most_ordered_cnt = ordered_by_cnt_desc[0][1]
        if most_ordered_cnt < 2:
            continue

        selected_menus = list(
            map(lambda x: x[0], filter(lambda x: x[1] == most_ordered_cnt, ordered_by_cnt_desc))
        )
        course_menus.extend(selected_menus)

    return sorted(course_menus)


"""
orders의 길이를 N, order의 길이를 최대 M, course 리스트의 길이를 K라고 했을 때,

1. for r in course loop: course의 모든 요소를 순회하므로 O(K)
    1) for order in orders loop: orders의 모든 요소를 순회하므로 course의 요소(r)에 대해 N번 반복됨.
        - sorted(order): 각 주문을 정렬하는 데 평균 O(Mlog M)의 시간 소요
        - combinations(order, r)
            : 각 주문에서 r개의 조합을 생성.
            : 최악의 경우 O(M combination r) 소요. (M과 r의 값에 따라 달라짐.)
            : 일반적으로 M combination r은 M^r보다 작거나 같음.
        
    2) orders loop 이후
        - Counter(r_course_menus).most_common()
            : r_course_menus의 길이는 orders 내의 각 주문에 대한 조합의 수의 합이므로, O(N * M^r)

2. sorted(course_menus): P가 결과물의 길이라고 했을 때, O(Plog P)

전체 시간 복잡도: O(K * N * M^r)
M과 r의 값에 크게 의존하며 r이 클수록 복잡도가 급격하게 증가함.
"""


orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
course = [2, 3, 4]
print(solution(orders, course))  # ["AC", "ACDE", "BCFG", "CDE"]

orders = ["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"]
course = [2, 3, 5]
print(solution(orders, course))  # ["ACD", "AD", "ADE", "CD", "XYZ"]

orders = ["XYZ", "XWY", "WXA"]
course = [2, 3, 4]
print(solution(orders, course))  # ["WX", "XY"]
