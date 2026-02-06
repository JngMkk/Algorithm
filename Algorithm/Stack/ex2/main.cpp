#include <iostream>
#include <stack>
#include <string>

using namespace std;

int main() {
    bool ok = true;
    stack<char> s;
    string input;
    cin >> input;

    for (char c : input) {
        if (c == '(') {
            s.push(c);
        } else {
            if (s.empty()) {
                ok = false;
                break;
            }
            s.pop();
        }
    }

    if (!s.empty()) ok = false;

    cout << (ok ? "Yes" : "No");

    return 0;
}

/*
입력으로 주어진 괄호 문자열이 올바른지, 그렇지 못한지를 판단하여 결과를 출력하는 프로그램을 작성하세요.
*/