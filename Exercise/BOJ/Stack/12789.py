def main():
    """
    while 루프 (temp 리스트에서 원소 제거)
        temp 리스트에서 원소를 제거하는 부분은 최악의 경우 N 버ㄴ 반복될 수 있음.
        이 while 루프는 for 루프 내부에 있지만, 각 원소는 temp에 한 번 추가되고 한 번만 제거되므로 총 연산 횟수는 N 번을 넘지 않음.

    외부의 for 루프는 N번 반복하고, 내부의 while 루프도 총 N번의 원소 제거 작업을 수행함.
    각 원소는 temp 리스트에 추가된 후 최대 한 번만 제거되므로, 2N번의 기본 연산이라고 볼 수 잇음.
    따라서, 전체 시간 복잡도는 O(N)이 됨.
    """
    input()
    origin = map(int, input().split())
    temp = []

    curr = 1
    for orig in origin:
        if orig != curr and temp and temp[-1] < orig:
            return "Sad"

        temp.append(orig)
        while temp and temp[-1] == curr:
            temp.pop()
            curr += 1

    return "Nice"


if __name__ == "__main__":
    print(main())
