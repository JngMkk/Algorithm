def solution(skill, skill_trees):
    """
    N: skill_trees 길이
    M: skill_trees 원소의 길이
    K: skill의 길이

    for loop => O(N)
    문자 치환 => O(M)
    문자 비교 => O(K), 문자의 길이가 최대 K이므로

        ===> O(N(M + K))
    """

    import re

    cnt = 0
    for skill_tree in skill_trees:
        s_tree = re.sub(f"[^{skill}]", "", skill_tree)
        if skill[: len(s_tree)] == s_tree:
            cnt += 1

    return cnt


skill = "CBD"
skill_trees = ["BACDE", "CBADF", "AECB", "BDA"]
print(solution(skill, skill_trees))  # 2
