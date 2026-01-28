#include <iostream>
#include <deque>

using namespace std;

int n;
deque<int> dq;

int main() {
    cin >> n;

    for (int i = 1; i < n+1; i++) {
        dq.push_back(i);
    }

    while (n != 1) {
        dq.pop_front();
        dq.push_back(dq.front());
        dq.pop_front();
        n--;
    }

    cout << dq.front();

    return 0;
}

/*
1부터 N까지의 정수가 오름차순으로 정렬되어 있습니다. 이 수열을 정수가 하나만 남을 때까지 다음과 같은 동작을 반복하는 프로그램을 작성하세요.

1. 맨 앞의 정수를 제거합니다.
2. 그 후 남은 수열의 맨 앞의 정수를 맨 뒤로 이동시킵니다.
*/