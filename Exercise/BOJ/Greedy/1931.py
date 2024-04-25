"""
https://www.acmicpc.net/problem/1931

종료 시간을 기준으로 정렬
    : 회의가 빨리 끝나면 그 회의실을 다시 사용할 수 있는 시간이 빨리 돌아오기 때문에
        회의가 끝나는 시간을 우선적으로 고려하여 다음 회의를 시작함.

겹치지 않는 회의 선택
    : 회의를 선택할 때는 이미 진행 중인 회의가 끝나는 시간 이후에 시작하는 회의 중에서 가장 빨리 끝나는 회의를 선택함.

meetings 리스트 만들기: O(N)
정렬: O(N log N)
정렬된 리스트 순회: O(N)

전체 시간 복잡도: O(N log N)
"""

N = int(input())
meetings = [tuple(map(int, reversed(input().split()))) for _ in range(N)]
meetings.sort()
cnt = 0
curr = 0
for end, start in meetings:
    if start >= curr:
        cnt += 1
        curr = end

print(cnt)

"""
11
1 4
3 5
0 6
5 7
3 8
5 9
6 10
8 11
8 12
2 13
12 14
"""
