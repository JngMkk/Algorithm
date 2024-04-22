def solution(str1: str, str2: str) -> int:
    from collections import Counter

    def clean_str(string: str) -> "list[str]":
        arr = []
        string = string.lower()
        for i in range(len(string) - 1):
            s = string[i : i + 2]
            if s.isalpha():
                arr.append(s)

        return arr

    arr1 = clean_str(str1)
    arr2 = clean_str(str2)

    if not arr1 and not arr2:
        return 65536

    counter1 = Counter(arr1)
    counter2 = Counter(arr2)
    n_inters = sum((counter1 & counter2).values())
    n_unions = sum((counter1 | counter2).values())

    return int(n_inters / n_unions * 65536)


str1 = "FRANCE"
str2 = "french"
print(solution(str1, str2))  # 16384

str1 = "handshake"
str2 = "shake hands"
print(solution(str1, str2))  # 65536

str1 = "aa1 + aa2"
str2 = "AAAA12"
print(solution(str1, str2))  # 43690

str1 = "E = M * C ^ 2"
str2 = "e = m * c ^ 2"
print(solution(str1, str2))  # 65536
