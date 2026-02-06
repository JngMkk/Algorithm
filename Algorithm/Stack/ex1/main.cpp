#include <iostream>
#include <vector>
#include <string>

using namespace std;

int n;

int main() {
    cin >> n;

    vector<int> arr;
    for (int i = 0; i < n; i++) {
        string command;
        cin >> command;
        if (command == "push") {
            int x;
            cin >> x;
            arr.push_back(x);
        } else if (command == "pop") {
            if (arr.empty())
                continue;
            cout << arr.back() << endl;
            arr.pop_back();
        } else if (command == "size") {
            cout << arr.size() << endl;
        } else if (command == "empty") {
            cout << arr.empty() << endl;
        } else {
            if (arr.empty())
                continue;
            cout << arr.back() << endl;
        }
    }
    
    return 0;
}

/**
 * push(E)
 *  맨 위에 데이터 E를 추가함
 * 
 * size()
 *  현재 stack에 들어 있는 데이터의 수를 반환
 * 
 * empty()
 *  현재 stack이 비어있다면 true, 아니라면 false를 반환함
 * 
 * top()
 *  stack의 가장 위에 있는 데이터 반환
 * 
 * pop()
 *  stack의 가장 위에 있는 데이터를 뺌.
 */