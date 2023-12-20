def solution(book_time: list[list[str]]) -> int:
    from heapq import heappop, heappush

    def convert_time(_time: str) -> int:
        hours, minutes = map(int, _time.split(":"))
        return 60 * hours + minutes

    book_time.sort()
    rooms = []
    for start, end in book_time:
        e = convert_time(end)
        if rooms:
            min_check_out = heappop(rooms)
            s = convert_time(start)
            if s < min_check_out + 10:
                heappush(rooms, min_check_out)
            heappush(rooms, e)
        else:
            heappush(rooms, e)

    return len(rooms)


def solution2(book_time: list[list[str]]) -> int:
    """
    전체 시간을 테이블로 표현하고,
    입실 시간에 +1 퇴실 시간 + 10(청소 시간)에 -1해서 누적합으로 구하는 방법

    해당 함수는 O(N) 위 함수는 O(NlogN)이므로 해당 함수가 일반적으로 더 효율적이라 볼 수 있음.
    """

    def convert_time(_time: str) -> int:
        hours, minutes = map(int, _time.split(":"))
        return 60 * hours + minutes

    minutes = [0 for _ in range(24 * 60 + 10)]
    for start, end in book_time:
        s = convert_time(start)
        e = convert_time(end)
        minutes[s] += 1
        minutes[e + 10] += -1

    num = 0
    for i in range(len(minutes)):
        num += minutes[i]
        minutes[i] = num

    return max(minutes)


book_time = [
    ["15:00", "17:00"],
    ["16:40", "18:20"],
    ["14:20", "15:20"],
    ["14:10", "19:20"],
    ["18:20", "21:20"],
]
print(solution(book_time))  # 3

book_time = [["09:10", "10:10"], ["10:20", "12:20"]]
print(solution(book_time))  # 1

book_time = [["10:20", "12:30"], ["10:20", "12:30"], ["10:20", "12:30"]]
print(solution(book_time))  # 3
