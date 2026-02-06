#include <iostream>
#include <vector>
#include <queue>

using std::cout;
using std::endl;
using std::vector;
using std::queue;

void bfs(const vector<vector<int>>& graph, int start, vector<int>& visited) {
    queue<int> q;

    q.push(start);
    visited[start] = 1;
    
    while (!q.empty()) {
        int vertex = q.front();
        q.pop();
        cout << vertex << " ";

        for (int v : graph[vertex]) {
            if (!visited[v]) {
                q.push(v);
                visited[v] = 1;
            }
        }
    }
}

int main() {
    vector<vector<int>> graph = { {}, { 2, 3, 8 }, { 1, 7 }, { 1, 4, 5 }, { 3, 5 }, { 3, 4 }, { 7 }, { 2, 6, 8 }, { 1, 7 } };
    vector<int> visited(9, 0);
    bfs(graph, 1, visited);
    cout << endl;

    return 0;
}