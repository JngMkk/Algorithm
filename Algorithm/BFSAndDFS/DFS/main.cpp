#include <iostream>
#include <vector>

using std::cout;
using std::endl;
using std::vector;

void dfs(const vector<vector<int>>& graph, int vertex, vector<int>& visited) {
    visited[vertex] = 1;
    cout << vertex << " ";
    for (int v : graph[vertex]) {
        if (!visited[v]) {
            dfs(graph, v, visited);
        }
    }
}

int main() {
    vector<vector<int>> graph = { {}, { 2, 3, 8 }, { 1, 7 }, { 1, 4, 5 }, { 3, 5 }, { 3, 4 }, { 7 }, { 2, 6, 8 }, { 1, 7 } };
    vector<int> visited(9, 0);
    dfs(graph, 1, visited);
    cout << endl;

    return 0;
}