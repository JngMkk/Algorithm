def solution(s: str) -> "list[int]":
#     from collections import Counter

#     counter: "Counter[int]" = Counter()
#     num = ""
#     for _str in s:
#         if _str.isdigit():
#             num += _str
#         else:
#             if num:
#                 counter[int(num)] += 1
#                 num = ""

#     return list(map(lambda x: x[0], counter.most_common()))

