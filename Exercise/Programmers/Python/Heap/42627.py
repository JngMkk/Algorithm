def solution(jobs: list[list[int]]):
    from heapq import heappop, heappush

    heap_q = []  # exec time이 짧은 순으로 대기 큐 생성
    time_total = 0  # process waiting time + process exec time
    time_now = -1  # 현재 하드 디스크 I/O 작업이 없는 경우로 초기화

    jobs.sort(reverse=True)
    N = len(jobs)

    while jobs or heap_q:
        if jobs and jobs[-1][0] <= time_now:  # 요청이 I/O 작업 중에 들어온 경우
            req_time, exec_time = jobs.pop()  # 요청 시점이 가장 가까운 process 꺼냄
            heappush(heap_q, (exec_time, req_time))  # 대기 큐에 삽입
        elif heap_q:  # 대기 큐에 process가 있다면
            exec_time, req_time = heappop(heap_q)
            time_total += time_now - req_time + exec_time  # 현재 시점 - 요청 시점 + 실행 시간
            time_now += exec_time  # 현재 시점에서 실제 실행 시간 덧셈
        else:  # 현재 하드 디스크 I/O 작업이 없을 경우 다음 요청 시점으로 현재 시점을 update (I/O 작업 중으로)
            time_now = jobs[-1][0]

    return time_total // N  # 평균 및 소수점 버리기


"""
1. sort() 메서드: O(N * log N)
2. while loop
    - heappush(): O(log M)
    - heappop(): O(log M)
    - 루프의 총 시간 복잡도는 작업 목록 길이 N과 heap queue의 연산에 의해 결정됨.
    - heap queue의 최대 크기는 N이므로, 각 힙 연산의 복잡도는 최대 O(log N)
    - 따라서 이 루프의 총 시간 복잡도는 O(N * log N)

전체 시간 복잡도: O(N * log N)
"""


jobs = [[0, 3], [1, 9], [2, 6]]
print(solution(jobs))
