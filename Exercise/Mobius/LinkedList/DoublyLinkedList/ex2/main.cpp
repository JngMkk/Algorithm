#include <iostream>
#include <list>
#include <string>

using namespace std;

int main() {
    int n;
    int m;
    string bread;
    list<char> lst;
    
    cin >> n >> m;
    cin >> bread;
    for (char c : bread) {
        lst.push_back(c);
    }

    list<char>::iterator it = lst.end();
    for (int i = 0; i < m; i++) {
        char command;
        cin >> command;
        if (command == 'P') {
            char element;
            cin >> element;
            lst.insert(it, element);
        } else if (command == 'L') {
            if (it == lst.begin())
                continue;
            it--;
        } else if (command == 'R') {
            if (it == lst.end())
                continue;
            it++;
        } else {
            if (it == lst.end())
                continue;
            it = lst.erase(it);
        }
    }

    for (char c : lst) {
        cout << c;
    }
    cout << endl;

    return 0;
}

/*
소문자 알파벳이 적혀있는 식빵들이 일렬로 나열되어 있습니다.
황금비율 토스트를 만들기 위해서는 레시피에 적혀있는 대로 움직이고 기존에 주어진 식빵들 사이에 새로운 식빵을 추가하거나 빼야 합니다.
아무나 따라 할 수 없도록 만들어진 레시피는 특정 룰과 암호 명령어로 이루어져 있습니다.

이 레시피에는 가리키는 위치 ⬆️ 라는 개념이 존재합니다. 가리키는 위치 ⬆️는 빵들의 맨 앞이거나, 맨 뒤이거나, 빵과 빵 사이뿐입니다.
즉, 빵의 개수가 총 T개라면, 레시피가 가리킬 수 있는 위치는 총 T+1 곳입니다. 단, 가리키는 위치 ⬆️는 처음에 모든 빵의 맨 마지막에 위치하고 있습니다.

'L'이 적혀있다면 가리키는 위치 ⬆️를 바로 앞에 있는 빵을 건너뛴 위치로 변경합니다. 만약, 이미 빵들의 맨 앞이라면 무시합니다.
'R'이 적혀있다면 가리키는 위치 ⬆️를 바로 뒤에 있는 빵을 건너뛴 위치로 변경합니다. 만약, 이미 빵들의 맨 뒤라면 무시합니다.
'D'가 적혀있다면 가리키는 위치 ⬆️의 바로 뒤에 있는 빵을 제거합니다. 만약, 이미 빵들의 맨 뒤라면 무시합니다.
'P &'가 적혀있다면 가리키는 위치 ⬆️에 &라는 문자가 적혀있는 식빵을 추가합니다. 이후 가리키는 위치 ⬆️는 추가된 문자 & 바로 뒤가 됩니다.
*/