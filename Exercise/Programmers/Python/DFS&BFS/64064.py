def solution(user_ids, banned_ids):
    def get_bannable_id_indices(banned_id, len_banned_id):
        bannable_ids = []
        for idx, user_id in enumerate(user_ids):
            if len(user_id) != len_banned_id:
                continue

            flag = 1
            for banned_char, user_char in zip(banned_id, user_id):
                if banned_char != "*" and banned_char != user_char:
                    flag = 0
                    break
            if flag:
                bannable_ids.append(idx)

        """
        길이가 짧은 리스트부터 처리하면, 일치하는 경우의 수가 적기 때문에 조합을 빠르게 걸러낼 수 있음. 즉, 더 빨리 실패 경로를 확인하고 불필요한 탐색을 줄일 수 있음.
        길이가 짧은 리스트를 먼저 처리함으로써, 후속 단계에서 이미 선택된 아이디들을 제외할 수 있어서 전체적으로 고려해야 할 경우의 수가 감소.
        더 빠른 성공 경로 발견: 제한된 선택지를 가진 불량 사용자 아이디부터 매칭을 시작하면, 유효한 제재 아이디 목록을 더 빠르게 확인할 수 있음.
        """
        return sorted(bannable_ids, key=len)

    def count_banned_ids():
        banned_map = [
            get_bannable_id_indices(banned_id, len(banned_id)) for banned_id in banned_ids
        ]
        n = len(banned_map)
        cases = set()

        def dfs(curr=[], idx=0):
            if idx == n:
                cases.add(tuple(sorted(curr)))
                return

            for user in banned_map[idx]:
                if user not in curr:
                    dfs(curr + [user], idx + 1)

        dfs()
        return len(cases)

    return count_banned_ids()


user_ids = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
banned_ids = ["fr*d*", "abc1**"]
print(solution(user_ids, banned_ids))  # 2

user_ids = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
banned_ids = ["*rodo", "*rodo", "******"]
print(solution(user_ids, banned_ids))  # 2

user_ids = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
banned_ids = ["fr*d*", "*rodo", "******", "******"]
print(solution(user_ids, banned_ids))  # 3
