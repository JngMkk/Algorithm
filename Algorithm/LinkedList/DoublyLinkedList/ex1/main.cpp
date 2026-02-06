#include <iostream>
#include <list>
#include <string>

using namespace std;

int main() {
    int n;
    list<int> lst;
    
    cin >> n;

    for (int i = 0; i < n; i++) {
        string command;
        cin >> command;

        if (command == "push_front") {
            int x;
            cin >> x;
            lst.push_front(x);
        } else if (command == "push_back") {
            int x;
            cin >> x;
            lst.push_back(x);
        } else if (command == "pop_front") {
            int x = lst.front();
            lst.pop_front();
            cout << x << endl;
        } else if (command == "pop_back") {
            cout << lst.back() << endl;
            lst.pop_back();
        } else if (command == "size") {
            cout << lst.size() << endl;
        } else if (command == "empty") {
            cout << lst.empty() << endl;
        } else if (command == "front") {
            cout << lst.front() << endl;
        } else {
            cout << lst.back() << endl;
        }
    }

    return 0;
}

/**
 * push_front(E)
 *  맨 앞에 데이터 E를 추가함
 * 
 * push_back(E)
 *  맨 뒤에 데이터 E를 추가함
 * 
 * pop_front()
 *  맨 앞에 있는 데이터를 뺌. C++에서의 list는 pop_front() 호출 시 삭제만 할 뿐, 해당 값을 반환하지 않음.
 *  이는 C++의 철학 상, 하나의 함수는 하나의 역할만 해야한다는 점과 안정성 측면에서 이렇게 설계되어져 있음.
 * 
 * pop_back()
 *  맨 뒤에 있는 데이터를 뺌.
 * 
 * size()
 *  현재 list에 들어있는 데이터의 수를 반환.
 * 
 * empty()
 *  list가 비어있다면 true, 아니라면 false
 * 
 * front()
 *  맨 앞의 데이터를 반환
 * 
 * back()
 *  맨 뒤 데이터를 반환
 */