def main():
    from collections import Counter

    _, target = tuple(map(int, input().split()))
    counter = Counter(map(int, input().split()))
    max_h = max(counter)
    min_h = 0
    while min_h <= max_h:
        mid_h = (min_h + max_h) // 2
        total = sum(
            map(lambda item: (item[0] - mid_h) * item[1] if item[0] > mid_h else 0, counter.items())
        )
        if total < target:
            max_h = mid_h - 1
        else:
            min_h = mid_h + 1

    return max_h


if __name__ == "__main__":
    print(main())


"""
위 함수가 해당 문제에선 더욱 효율적으로 동작할 수 있음.
그 이유는, 배열 입력 원소들의 값이 매우 크고, 중복될 가능성이 있기 때문임.
Counter를 사용해서 중복 원소들을 한꺼번에 계산하면 시간적으로 이득볼 수 있음.
"""


def main():
    _, target = tuple(map(int, input().split()))
    arr = tuple(map(int, input().split()))
    max_h = max(arr)
    min_h = 0
    while min_h <= max_h:
        mid_h = (min_h + max_h) // 2
        total = sum((map(lambda x: x - mid_h if x > mid_h else 0, arr)))
        if total < target:
            max_h = mid_h - 1
        else:
            min_h = mid_h + 1

    return max_h


if __name__ == "__main__":
    print(main())
