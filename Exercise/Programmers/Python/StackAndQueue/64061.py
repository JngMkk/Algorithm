def solution(board: "list[list[int]]", moves: "list[int]") -> int:
    """
    내부 루프가 일찍 종료되더라도 최악의 경우(모든 경우에 대해 모든 행을 순회해야 하거나 마지막 해에 도달할 때까지 반복해야 하는 경우)
    시간 복잡도는 O(len(moves) x len(board))
    """

    rows = len(board)
    stack: "list[int]" = []
    cnt = 0
    for move in moves:
        for row in range(rows):
            if board[row][move - 1] != 0:
                if stack and stack[-1] == board[row][move - 1]:
                    stack.pop()
                    cnt += 2
                else:
                    stack.append(board[row][move - 1])

                board[row][move - 1] = 0
                break

    return cnt


def solution2(board: "list[list[int]]", moves: "list[int]") -> int:
    """
    초기화: 각 열의 최상단 인형 위치를 설정하는데 O(row x col) 소요
    플레이: 각 move는 O(1) 시간에 처리되므로 O(len(moves))
    """

    rows = len(board)
    cols = len(board[0])

    # * crain 번호마다 최상단에 뽑힐 인형 행 인덱스 저장
    top_pointer = [rows] * cols

    for col in range(cols):
        for row in range(rows):
            if board[row][col] != 0:
                top_pointer[col] = row
                break

    stack: "list[int]" = []
    cnt = 0
    for move in moves:
        col = move - 1
        if top_pointer[col] < rows:
            doll = board[top_pointer[col]][col]
            top_pointer[col] += 1

            if stack and stack[-1] == doll:
                stack.pop()
                cnt += 2
            else:
                stack.append(doll)

    return cnt


def solution3(board: "list[list[int]]", moves: "list[int]") -> int:
    """위 함수와 시간 복잡도는 동일함"""

    cols = len(board[0])

    # * crain 번호마다 뽑힐 인형 순서대로 저장. 빈 리스트면 뽑힐 인형 없음.
    crain: "list[list[int]]" = [[] for _ in range(cols)]
    stack: "list[int]" = []
    cnt = 0
    for bor in reversed(board):
        for c in range(cols):
            if bor[c] > 0:
                crain[c].append(bor[c])

    for move in moves:
        if crain[move - 1]:
            item = crain[move - 1].pop()
            if stack and item == stack[-1]:
                stack.pop()
                cnt += 2
            else:
                stack.append(item)

    return cnt


board = [[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [0, 2, 5, 0, 1], [4, 2, 4, 4, 2], [3, 5, 1, 3, 1]]
moves = [1, 5, 3, 5, 1, 2, 1, 4]  # 4
print(solution3(board, moves))
