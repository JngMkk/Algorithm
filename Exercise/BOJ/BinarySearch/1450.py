"""
2 1
1 1
-> 3

1 1
1
-> 2

1 2
1
-> 2

2 1
2 2
-> 1

2 2
1 1
-> 4

30 30
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
-> 1073741824
"""


def main():
    from itertools import combinations

    def __get_subsets(array):
        subsets = []
        for i in range(len(array) + 1):
            for comb in combinations(array, i):
                if (_sum := sum(comb)) <= c:
                    subsets.append(_sum)
        return subsets

    def __b_search(elem):
        start = 0
        end = l_len
        while start < end:
            mid = (start + end) // 2
            if left_subsets[mid] + elem > c:
                end = mid
            else:
                start = mid + 1
        return start

    n, c = map(int, input().split())
    arr = list(map(int, input().split()))
    div = n // 2
    left_arr = arr[:div]
    right_arr = arr[div:]
    left_subsets = sorted(__get_subsets(left_arr))
    right_subsets = __get_subsets(right_arr)
    l_len = len(left_subsets)

    cnt = 0
    for elem in right_subsets:
        cnt += __b_search(elem)

    return cnt


if __name__ == "__main__":
    print(main())
