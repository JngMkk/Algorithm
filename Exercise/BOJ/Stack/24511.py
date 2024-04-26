def solution1():
    """
    O(N + M)
    """
    from collections import deque

    input()
    # A, B 입력 길이 N => O(N)
    queue = deque([B for A, B in zip(input().split(), input().split()) if A == "0"])
    input()
    C = input().split()

    elems = []
    # C의 입력 길이 M => O(M) appendleft, append, pop은 상수 시간.
    for elem in C:
        queue.appendleft(elem)
        elems.append(queue.pop())

    return " ".join(elems)


def solution2():
    """
    queue 자료구조를 사용하는 값들 중에 queuestack에 원소를 입력할 때마다 가장 마지막 큐의 값을 빼고 가장 앞 큐의 원소는 입력값으로 바뀌기 때문에
    queue 자료구조를 사용하는 값들을 reverse하면 입력 시 출력될 원소들이 정렬되고, 그 후 값들은 입력된 값 순서대로 나오므로, reverse한 후 입력된 값을 합쳐줌.
    """
    input()
    reversed_only_q_elems = [B for A, B in zip(input().split(), input().split()) if A == "0"][::-1]
    M = int(input())
    reversed_only_q_elems.extend(input().split())

    return " ".join(reversed_only_q_elems[:M])


if __name__ == "__main__":
    print(solution2())
