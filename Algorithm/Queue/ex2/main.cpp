#include <iostream>
#include <queue>

using namespace std;

int n, k;
queue<int> que;

int main() {
    cin >> n >> k;

    for (int i = 1; i < n+1; i++) {
        que.push(i);
    }

    while (!que.empty()) {
        for (int i = 0; i < k-1; i++) {
            que.push(que.front());
            que.pop();
        }

        cout << que.front() << " ";
        que.pop();
    }

    cout << endl;
    return 0;
}

/*
1번부터 N번까지 N명의 사람이 원을 이루면서 앉아있고, 양의 정수 K가 주어집니다.

다음의 연산을 N명의 사람들이 모두 제거될때까지 진행합니다.
1. 1번부터 순서대로 K번째 사람을 제거합니다.
2. 한 사람이 제거되면 남은 사람들로 원을 이루며 1번 연산을 과정을 반복합니다.

제거되는 사람의 번호를 순서대로 나열한 순열을 구하는 프로그램을 작성하세요.
*/