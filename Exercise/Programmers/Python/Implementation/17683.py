def solution(m: str, musicinfos: list[str]) -> str:
    def convert_sharp_to_alpha(pitches: str) -> str:
        """str.replace()로 대체할 수 있음."""

        last_idx = len(pitches) - 1
        ret = []
        for idx, pitch in enumerate(pitches):
            if pitch == "#":
                continue

            if idx != last_idx and pitches[idx + 1] == "#":
                ret.append(pitch_map[f"{pitch}#"])
            else:
                ret.append(pitch)

        return "".join(ret)

    def get_played_minutes(start: str, end: str) -> int:
        def get_minutes(_time: str) -> int:
            hours, minutes = map(int, _time.split(":"))
            return 60 * hours + minutes

        return get_minutes(end) - get_minutes(start)

    answer = "(None)"
    pitch_map = {"C#": "1", "D#": "2", "F#": "3", "G#": "4", "A#": "5", "E#": "6"}
    m = convert_sharp_to_alpha(m)
    max_played_minutes = 0
    for music_info in musicinfos:
        start, end, title, pitches = music_info.split(",")
        played_minutes = get_played_minutes(start, end)
        if max_played_minutes >= played_minutes:
            continue

        pitches = convert_sharp_to_alpha(pitches)
        quotient, remainder = divmod(played_minutes, len(pitches))
        played_pitches = pitches * quotient + pitches[:remainder]
        if m in played_pitches:
            max_played_minutes = played_minutes
            answer = title

    return answer


m = "ABCDEFG"
musicinfos = ["00:00,11:59,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF#"]
print(solution(m, musicinfos))  # "HELLO"

m = "CC#BCC#BCC#BCC#B"
musicinfos = ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]
print(solution(m, musicinfos))  # "FOO"

m = "ABC"
musicinfos = ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]
print(solution(m, musicinfos))  # "WORLD"
