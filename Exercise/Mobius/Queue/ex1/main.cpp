#include <iostream>
#include <queue>
#include <string>

using namespace std;

int n;
queue<int> que;

int main() {
    cin >> n;

    for (int i = 0; i < n; i++) {
        string command;
        cin >> command;
        if (command == "push") {
            int x;
            cin >> x;
            que.push(x);
        } else if (command == "pop") {
            cout << que.front() << endl;
            que.pop();
        } else if (command == "size") {
            cout << que.size() << endl;
        } else if (command == "empty") {
            cout << que.empty() << endl;
        } else {
            cout << que.front() << endl;
        }
    }

    return 0;
}