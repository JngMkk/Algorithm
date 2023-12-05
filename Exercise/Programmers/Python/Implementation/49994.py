def solution(dirs: str) -> int:
    move = {"U": (0, 1), "D": (0, -1), "L": (-1, 0), "R": (1, 0)}
    moved = set()

    cnt = 0
    x, y = 0, 0
    for dir in dirs:
        dx, dy = move[dir]
        nx, ny = x + dx, y + dy
        if nx < -5 or nx > 5 or ny < -5 or ny > 5:
            continue

        min_coord = min(x, nx), min(y, ny)
        max_coord = max(x, nx), max(y, ny)
        if (min_coord, max_coord) not in moved:
            moved.add((min_coord, max_coord))
            cnt += 1
        x = nx
        y = ny

    return cnt


"""
dirs의 길이를 N이라고 했을 때,

for dir in dirs loop
    - dirs의 모든 문자를 순회하므로 O(N)
    - move[dir]: 딕셔너리 조회 O(1)
    - 좌표 계산 및 경계 조건 확인: 단순 연산 O(1)
    - min, max: 단순 연산 O(1)
    - set 요소 추가: 해시 테이블을 사용하므로 평균적으로 O(1). 해시 충돌이 일어날 경우 O(N)

전체 시간 복잡도: O(N)
"""


dirs = "ULURRDLLU"
print(solution(dirs))  # 7
dirs = "LULLLLLLU"
print(solution(dirs))  # 7
