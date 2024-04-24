def solution2(relation: "list[list[str]]") -> int:
    """
    종합적으로, 이 함수의 시간 복잡도는 각 조합을 만들고 검사하는 데 O(2^cols <조합 생성> * (rows * cols) <유일성 검사> * cols <최소성 검사>).

    이 접근법은 모든 가능한 조합을 고려하기 때문에 상당히 비효율적임.
    특히 큰 데이터셋에서는 실행 시간이 매우 길어질 수 있음.

    개선 방법
        - 비트마스킹 사용: 각컬럼의 조합을 비트로 표현하여 조합을 더 빠르게 생성하고 관리할 수 있음
        - 최소성을 먼저 확인: 유일성을 확인하기 전에, 이미 발견된 후보키의 부분집합인지 먼저 확인하여 불필요한 유일성 검사를 줄임.
    """
    from itertools import combinations

    num_of_cols = len(relation[0])
    num_of_rows = len(relation)

    relation_T = [[relation[r][c] for r in range(num_of_rows)] for c in range(num_of_cols)]

    candidate_keys: "list[set]" = []
    for r in range(1, num_of_cols + 1):
        # * 조합 생성. num_of_cols가 최대 8개이므로 최악의 경우 -> 2^8 - 1 (255개)
        for comb in combinations([c for c in range(num_of_cols)], r):
            _set = set()

            # * 유일성 확인
            # * 각 조합에 대해 모든 행을 순회하면서 각 조합의 값들을 튜플로 만들어 집합에 추가함.
            # * 순회는 num_of_rows이며, 각 조합의 크기가 num_of_cols이므로, 이 작업의 복잡도는 O(r * c)
            for row in range(num_of_rows):
                elements = []
                for x in range(len(comb)):
                    elements.append(relation_T[comb[x]][row])
                _set.add(tuple(elements))
            if len(_set) == num_of_rows:
                comb_set = set(comb)
                flag = True

                # * 최소성 확인: 이미 발견된 후보키 집합들과의 비교를 통해 최소성을 확인함.
                # * 후보키의 개수가 'n'일 때, 각 조합마다 'n'번 비교를 수행하고, 각 비교의 복잡도는 num_of_cols임.
                for candi in candidate_keys:
                    if not candi - comb_set:
                        flag = False
                        break
                if flag:
                    candidate_keys.append(comb_set)

    return len(candidate_keys)


def solution(relation: "list[list[str]]") -> int:
    """
    O(2^cols * (k * cols + row * cols))
    """
    num_cols = len(relation[0])

    candidate_keys: "list[int]" = []

    # * 모든 컬럼의 조합을 비트로 표현
    # * 1부터 2^num_cols - 1까지 모든 조합을 생성 (비트마스킹 사용): O(2^cols)
    for i in range(1, 1 << num_cols):
        # * 최소성 검사: 현재 조합 i가 기존 후보키의 부분집합인지 검사
        # * 현재까지 발견된 후보키의 수를 k라 했을 때: O(k * cols)
        if any(i & key == key for key in candidate_keys):
            continue

        unique = True
        row_set = set()
        # * 유일성 검사: 해당 조합으로 모든 행이 유일한지 확인
        # * 각 행마다 cols개의 컬럼을 확인: O(rows * cols)
        for row in relation:
            # * 현재 조합의 컬럼으로만 데이터 튜플을 생성
            data = tuple(row[col] for col in range(num_cols) if i & (1 << col))
            if data in row_set:
                unique = False
                break
            row_set.add(data)

        # * 모든 행이 유일하면 이 조합은 후보키
        if unique:
            candidate_keys.append(i)

    return len(candidate_keys)


relation = [
    ["100", "ryan", "music", "2"],
    ["200", "apeach", "math", "2"],
    ["300", "tube", "computer", "3"],
    ["400", "con", "computer", "4"],
    ["500", "muzi", "music", "3"],
    ["600", "apeach", "music", "2"],
]
print(solution(relation))  # 2
