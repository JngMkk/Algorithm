"""
10 15
5 1 3 5 10 7 4 9 2 8
-> 2
"""


def main():
    n, s = map(int, input().split())
    arr = tuple(map(int, input().split()))

    start, end = 0, 0
    _sum = arr[0]
    min_interval = n + 1

    while end < n:
        if _sum >= s:
            if (interval := end - start + 1) < min_interval:
                min_interval = interval
            _sum -= arr[start]
            start += 1
        else:
            end += 1
            if end < n:
                _sum += arr[end]

    if min_interval == n + 1:
        return 0
    return min_interval


if __name__ == "__main__":
    print(main())
