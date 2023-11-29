def solution(bandage: list[int], health: int, attacks: list[list[int]]) -> int:
    t, x, y = bandage
    curr_health = health
    max_idx = len(attacks) - 1
    for r_idx, attack in enumerate(attacks, 1):
        l_time, damage = attack
        curr_health -= damage
        if curr_health <= 0:
            return -1

        if r_idx <= max_idx:
            r_time = attacks[r_idx][0]
            duration = r_time - l_time - 1
            if duration >= t:
                curr_health += (duration // t) * y

            curr_health += duration * x

            if curr_health > health:
                curr_health = health

    return curr_health


bandage = [5, 1, 5]
health = 30
attacks = [[2, 10], [9, 15], [10, 5], [11, 5]]
print(solution(bandage, health, attacks))  # 5

bandage = [3, 2, 7]
health = 20
attacks = [[1, 15], [5, 16], [8, 6]]
print(solution(bandage, health, attacks))  # -1

bandage = [4, 2, 7]
health = 20
attacks = [[1, 15], [5, 16], [8, 6]]
print(solution(bandage, health, attacks))  # -1

bandage = [1, 1, 1]
health = 5
attacks = [[1, 2], [3, 2]]
print(solution(bandage, health, attacks))  # 3
