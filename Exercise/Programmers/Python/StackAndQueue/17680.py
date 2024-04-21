def solution(cacheSize: int, cities: "list[str]") -> int:
    from collections import deque

    if cacheSize == 0:
        return len(cities) * 5

    cache: "deque[str]" = deque(maxlen=cacheSize)

    exec_time = 0
    for city in cities:
        city = city.lower()
        if city in cache:
            cache.remove(city)
            cache.append(city)
            exec_time += 1
        else:
            cache.append(city)
            exec_time += 5

    return exec_time


cacheSize = 3
cities = ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]
print(solution(cacheSize, cities))  #    50

cacheSize = 3
cities = ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]
print(solution(cacheSize, cities))  # 21

cacheSize = 2
cities = [
    "Jeju",
    "Pangyo",
    "Seoul",
    "NewYork",
    "LA",
    "SanFrancisco",
    "Seoul",
    "Rome",
    "Paris",
    "Jeju",
    "NewYork",
    "Rome",
]
print(solution(cacheSize, cities))  # 	60

cacheSize = 5
cities = [
    "Jeju",
    "Pangyo",
    "Seoul",
    "NewYork",
    "LA",
    "SanFrancisco",
    "Seoul",
    "Rome",
    "Paris",
    "Jeju",
    "NewYork",
    "Rome",
]
print(solution(cacheSize, cities))  # 	52

cacheSize = 2
cities = ["Jeju", "Pangyo", "NewYork", "newyork"]
print(solution(cacheSize, cities))  #    16

cacheSize = 0
cities = ["Jeju", "Pangyo", "Seoul", "NewYork", "LA"]
print(solution(cacheSize, cities))  #    25
