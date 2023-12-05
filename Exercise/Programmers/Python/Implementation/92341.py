def solution(fees: list[int], records: list[str]) -> list[int]:
    from math import ceil

    def calculate_minute(hour: int, minutes: int) -> int:
        return 60 * hour + minutes

    def process_car_in(hour: int, minutes: int, car_num: str) -> None:
        if car_num in car_minutes:
            car_minutes[car_num] += end_time - calculate_minute(hour, minutes)
        else:
            car_minutes[car_num] = end_time - calculate_minute(hour, minutes)
        return

    def process_car_out(hour: int, minutes: int, car_num: str) -> None:
        car_minutes[car_num] = car_minutes[car_num] - (end_time - calculate_minute(hour, minutes))
        return

    car_minutes = {}
    end_time = calculate_minute(23, 59)
    for record in records:
        time, car_num, io = record.split(" ")
        hour, minutes = map(int, time.split(":"))
        if io == "IN":
            process_car_in(hour, minutes, car_num)
        else:
            process_car_out(hour, minutes, car_num)

    answer = []
    for key in sorted(car_minutes.keys()):
        over_minutes = car_minutes[key] - fees[0]
        fee = fees[1]
        if over_minutes > 0:
            fee += ceil(over_minutes / fees[2]) * fees[3]
        answer.append(fee)

    return answer


"""
records 리스트 길이를 N이라고 했을 때,

1. for record in records 루프
    - 모든 요소를 순회: O(N)
    - split(): 상수 시간, 즉 O(1)에 가까움.
    - calculate_minute(): 연산 또한 단순 계산이므로 O(1)
    - 두 process 함수
        : 딕셔너리 조회 및 갱신
        : 딕셔너리 연산은 평균적으로 O(1)이지만 해시 충돌이 자주 일어나면(최악의 경우라면) O(N)

2. for key in sorted(car_minutes.key()) 루프
    - sorted() 함수: 딕셔너리 키의 개수를 M이라고 했을 때, O(Mlog M), 모든 레코드가 서로 다른 key에 할당될 때 최대 N
    - 나머지 연산(ceil 함수 포함): 단순 계산이므로 O(1)

결과적으로 O(N) 루프와 O(Mlog M) 루프의 복잡도를 합친 것이 전체 시간 복잡도.
따라서, 전체 시간 복잡도는 O(N + Mlog M) => O(Nlog N)
"""


fees = [180, 5000, 10, 600]
records = [
    "05:34 5961 IN",
    "06:00 0000 IN",
    "06:34 0000 OUT",
    "07:59 5961 OUT",
    "07:59 0148 IN",
    "18:59 0000 IN",
    "19:09 0148 OUT",
    "22:59 5961 IN",
    "23:00 5961 OUT",
]
print(solution(fees, records))  # [14600, 34400, 5000]

fees = [120, 0, 60, 591]
records = ["16:00 3961 IN", "16:00 0202 IN", "18:00 3961 OUT", "18:00 0202 OUT", "23:58 3961 IN"]
print(solution(fees, records))  # [0, 591]

fees = [1, 461, 1, 10]
records = ["00:00 1234 IN"]
print(solution(fees, records))  # [14841]
