def solution(files):
    splited = []
    for file in files:
        head = []
        num = []
        idx = 0
        n = len(file)
        while not file[idx].isdecimal():
            head.append(file[idx])
            idx += 1
        while idx < n and file[idx].isdecimal():
            num.append(file[idx])
            idx += 1
        splited.append(("".join(head), "".join(num), file[idx:]))

    return list(
        map(
            lambda x: "".join(x),
            sorted(splited, key=lambda x: (x[0].lower(), int(x[1]))),
        )
    )


def solution(files):
    import re

    num_sorted = sorted(files, key=lambda file: int(re.findall("\d+", file)[0]))
    return sorted(num_sorted, key=lambda file: re.split("\d+", file.lower())[0])


files = ["F-5", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]
print(
    solution(files)
)  # ["img1.png", "IMG01.GIF", "img02.png", "img2.JPG", "img10.png", "img12.png"]
files = ["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]
print(
    solution(files)
)  # ["A-10 Thunderbolt II", "B-50 Superfortress", "F-5 Freedom Fighter", "F-14 Tomcat"]
