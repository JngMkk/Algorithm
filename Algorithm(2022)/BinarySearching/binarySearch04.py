"""
    최적화 문제를 결정 문제("예" 혹은 "아니오")로 바꾸어 해결하는 기법.
        - 예시: 특정한 조건을 만족하는 가장 알맞은 값을 빠르게 찾는 최적화 문제

    일반적으로 코딩 테스트에서 파라메트릭 서치 문제는 이진 탐색을 이용하여 해결할 수 있음.
"""

"""
    문제

        사용자는 여행 가신 부모님을 대신해서 떡집 일을 하기로 했음. 오늘은 떡볶이 떡을 만드는 날.
        사용자의 떡볶이 떡은 재밌게도 떡볶이 떡의 길이가 일정하지 않음.
        대신 한 봉지 안에 들어가는 떡의 총 길이는 절단기로 잘라서 맞춰줌.

        절단기에 높이 H를 지정하면 줄지어진 떡을 한 번에 절단함.
        높이 H보다 긴 떡은 H 위의 부분이 잘릴 것이고, 낮은 떡은 잘리지 않음.

        예를 들어 높이가 19, 14, 10, 17cm인 떡이 나란히 있고 절단기 높이를 15cm로 지정하면 자른 뒤 떡의 높이는 15, 14, 10, 15가 될 것.
        잘린 떡의 길이는 차례대로 4, 0, 0, 2cm임. 손님은 6cm만큼의 길이를 가져감.

        손님이 왔을 때 요청한 총 길이가 M일 때 적어도 M만큼의 떡을 얻기 위해 절단기에 설정할 수 있는 높이의 최댓값을 구하는 프로그램 작성.

        첫 줄에 떡의 개수와 M.

        입력 예시
        4 6
        19 15 10 17
"""

# 나의 풀이
n, m = map(int, input().split())
cm = list(map(int, input().split()))
tmp = []


def search(array, target, start, maxH):
    if start > maxH:
        return None
    mid = (start + maxH) // 2

    res = 0
    for a in array:
        if a - mid > 0:
            res += a - mid

    if res >= target:
        tmp.append(mid)
        search(array, target, mid + 1, maxH)

    else:
        search(array, target, start, mid - 1)

    return max(tmp)


print(search(cm, m, 1, max(cm)))


"""
    문제 해결 아이디어

        적절한 높이를 찾을 때까지 이진 탐색을 수행하여 높이 H를 반복해서 조정하면 됨.

        현재 이 높이로 자르면 조건을 만족할 수 있는가?를 확인한 뒤에 조건의 만족 여부에 따라서 탐색 범위를 좁혀서 해결할 수 있음.

        절단기의 높이는 0부터 10억까지의 정수 중 하나임
            - 이렇게 큰 탐색 범위를 보면 가장 먼저 이진 탐색을 떠올려야 함
"""

# 해답
n, m = map(int, input().split())
array = list(map(int, input().split()))

start = 0
end = max(array)

result = 0
while start <= end:
    total = 0
    mid = (start + end) // 2
    for x in array:
        if x > mid:
            total += x - mid

    if total < m:
        end = mid - 1

    else:
        result = mid
        start = mid + 1

print(result)
