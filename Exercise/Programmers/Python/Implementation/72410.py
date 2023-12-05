def solution(new_id: str) -> str:
    from re import sub

    # 1. 소문자 치환
    new_id = new_id.lower()

    # 2. 소문자, 숫자, 빼기, 밑줄, 마침표 제외 모두 제거
    new_id = sub(r"[^a-z0-9\-_.]", "", new_id)

    # 3. 연속하는 마침표 하나로 합치기
    new_id = sub(r"[.]{2,}", ".", new_id)

    # 4. 처음 끝 마침표 제거
    new_id = sub(r"^[.]|[.]$", "", new_id)

    # 5. 빈 문자열이면 a 추가
    if not new_id:
        new_id = "a"

    # 6. 16자 이상이면 15 이후로 제거 및 마지막 마침표 제거
    new_id = new_id[:15]
    new_id = sub(r"[.]$", "", new_id)

    # 7. 2자 이하라면, 3자가 될 때까지 마지막 문자 끝에 붙이기
    while len(new_id) < 3:
        new_id += new_id[-1]

    return new_id


new_id = "...!@BaT#*..y.abcdefghijklm"
print(solution(new_id))  # "bat.y.abcdefghi"

new_id = "z-+.^."
print(solution(new_id))  # "z--"

new_id = "=.="
print(solution(new_id))  # "aaa"

new_id = "123_.def"
print(solution(new_id))  # "123_.def"

new_id = "abcdefghijklmn.p"
print(solution(new_id))  # "abcdefghijklmn"
