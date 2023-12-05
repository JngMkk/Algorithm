def solution(numbers: list[int]) -> list[int]:
    answer = [-1] * len(numbers)
    idx_stack = []
    for idx, num in enumerate(numbers):
        while idx_stack and numbers[idx_stack[-1]] < num:
            answer[idx_stack.pop()] = num
        idx_stack.append(idx)

    return answer


"""
numbers 길이를 N이라고 했을 때,

for loop
    - 모든 요소를 한 번씩 순회 O(N)
    - while loop
        : 각 요소는 최대 한 번 스택에 push되고 한 번 pop됨. push, pop은 O(1)
        : for loop 내의 while loop이 numbers의 각 요소에 대해 여러 번 실행될 수는 있지만,
          각 요소가 스택에 들어가고 나오는 것은 최대 한 번씩만 발생함.
          그러므로, 전체적인 연산 횟수는 2*N 이하가 됨.

전체 시간 복잡도: O(2N) => O(N)
입력 리스트의 크기에 선형적으로 증가함
"""


numbers = [2, 3, 3, 5]
print(solution(numbers))  # [3, 5, 5, -1]

numbers = [9, 1, 5, 3, 6, 2]
print(solution(numbers))  # [-1, 5, 6, 6, -1, -1]
