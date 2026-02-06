#include <iostream>
#include <deque>
#include <string>

using namespace std;

int n;
deque<int> dq;

int main() {
    cin >> n;

    for (int i = 0; i < n; i++) {
        string command;
        cin >> command;
        if (command == "push_front") {
            int x;
            cin >> x;
            dq.push_front(x);
        } else if (command == "push_back") {
            int x;
            cin >> x;
            dq.push_back(x);
        } else if (command == "pop_front") {
            cout << dq.front() << endl;
            dq.pop_front();
        } else if (command == "pop_back") {
            cout << dq.back() << endl;
            dq.pop_back();
        } else if (command == "size") {
            cout << dq.size() << endl;
        } else if (command == "empty") {
            cout << dq.empty() << endl;
        } else if (command == "front") {
            cout << dq.front() << endl;
        } else {
            cout << dq.back() << endl;
        }
    }
    return 0;
}