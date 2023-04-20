# https://school.programmers.co.kr/learn/courses/30/lessons/17680

"""
문제 설명
캐시
지도개발팀에서 근무하는 제이지는 지도에서 도시 이름을 검색하면 해당 도시와 관련된 맛집 게시물들을 데이터베이스에서 읽어 보여주는 서비스를 개발하고 있다.
이 프로그램의 테스팅 업무를 담당하고 있는 어피치는 서비스를 오픈하기 전 각 로직에 대한 성능 측정을 수행하였는데, 제이지가 작성한 부분 중 데이터베이스에서 게시물을 가져오는 부분의 실행시간이 너무 오래 걸린다는 것을 알게 되었다.
어피치는 제이지에게 해당 로직을 개선하라고 닦달하기 시작하였고, 제이지는 DB 캐시를 적용하여 성능 개선을 시도하고 있지만 캐시 크기를 얼마로 해야 효율적인지 몰라 난감한 상황이다.

어피치에게 시달리는 제이지를 도와, DB 캐시를 적용할 때 캐시 크기에 따른 실행시간 측정 프로그램을 작성하시오.

입력 형식
캐시 크기(cacheSize)와 도시이름 배열(cities)을 입력받는다.
cacheSize는 정수이며, 범위는 0 ≦ cacheSize ≦ 30 이다.
cities는 도시 이름으로 이뤄진 문자열 배열로, 최대 도시 수는 100,000개이다.
각 도시 이름은 공백, 숫자, 특수문자 등이 없는 영문자로 구성되며, 대소문자 구분을 하지 않는다. 도시 이름은 최대 20자로 이루어져 있다.
출력 형식
입력된 도시이름 배열을 순서대로 처리할 때, "총 실행시간"을 출력한다.
조건
캐시 교체 알고리즘은 LRU(Least Recently Used)를 사용한다.
cache hit일 경우 실행시간은 1이다.
cache miss일 경우 실행시간은 5이다.
입출력 예제
캐시크기(cacheSize)	도시이름(cities)	실행시간
3	["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]	50
3	["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]	21
2	["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]	60
5	["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]	52
2	["Jeju", "Pangyo", "NewYork", "newyork"]	16
0	["Jeju", "Pangyo", "Seoul", "NewYork", "LA"]	25
"""


"""
LRU 알고리즘

- 가장 오랜 시간 사용되지 않은 페이지를 교체하는 운영체제의 페이지 교체 정책 알고리즘이다.

- 주로 캐시에서 메모리를 다루기 위해 사용된다.

- 캐시는 크게 보면 웹 서비스부터, 작게는 CPU가 RAM이나 Disk에 접근할 때.. 등 광범위하게 사용됨.

- 이러한 캐시들은 자원이 한정되어있으며, 한정된 자원 내에서 빠르게 데이터 접근이 가능해야 한다.

- 따라서 어떤 데이터를 남기고, 어떤 데이터를 지울지에 대한 알고리즘이 필요.

- 여기서 오래 참조되지 않은 데이터는 내보내는 '시간(temporal) 지역성'의 성질을 가지는 알고리즘이다.

장점
    - 빠른 액세스

        가장 최근에 사용한 아이템부터 가장 적게 사용한 아이템까지 정렬된다.

        따라서 두 아이템에 접근할 경우, O(n)의 시간 복잡도를 가진다.

    - 빠른 Update

        하나의 아이템에 엑세스 할때마다 업데이트 되며, O(n)의 시간 복잡도를 가진다.

단점
    - 많은 공간 차지

        n개의 아이템을 저장하는 LRU는 n의 크기를 가지는 1개의 Linked-list와(혹은 Queue) 이를 추적하기 위한 n의 크기를 가지는 1개의 hash-map이 필요하다.

        이는 O(n)의 복잡도를 가지지만, 2개의 데이터구조를 사용해야 한다는 단점이 있다.
"""


def solution(cacheSize, cities):
    if cacheSize == 0:
        return len(cities) * 5

    time = 0
    cache = []
    for city in cities:
        l = city.lower()
        if l in cache:
            cache.remove(l)
            cache.append(l)
            time += 1
            continue

        if len(cache) == cacheSize:
            cache.pop(0)
        time += 5
        cache.append(l)

    return time


# ================================================

from collections import deque


def solution(cacheSize, cities):
    if cacheSize == 0:
        return len(cities) * 5

    time = 0
    # maxlen: 초과하면 popleft() 하고 append
    cache = deque(maxlen=cacheSize)

    for city in cities:
        l = city.lower()
        if l in cache:
            cache.remove(l)
            cache.append(l)
            time += 1
        else:
            cache.append(l)
            time += 5
    return time
