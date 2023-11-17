def solution(players: list[str], callings: list[str]) -> list[str]:
    order_dic = {player: idx for idx, player in enumerate(players)}

    for calling in callings:
        calling_idx = order_dic[calling]
        prev_idx = calling_idx - 1
        order_dic[players[prev_idx]] = calling_idx
        order_dic[calling] = prev_idx
        players[prev_idx], players[calling_idx] = (
            players[calling_idx],
            players[prev_idx],
        )

    return players


players = ["a", "b", "c", "d", "e"]
callings = ["d", "d", "e", "e"]
print(solution(players, callings))
# ["a", "d", "e", "b","c"]
