#include <iostream>
#include <vector>

#include "sort.h"

void PrintArr(std::vector<int>& arr) {
    for (int num : arr) {
        std::cout << num << " ";
    }
    std::cout << "\n";
}

int main() {
    const int initialValue = 5;
    std::vector<int> arr, arr2, arr3;
    
    arr.reserve(initialValue); arr2.reserve(initialValue); arr3.reserve(initialValue);
    
    for (int i = initialValue; i > 0; i--) {
        arr.push_back(i); arr2.push_back(i); arr3.push_back(i);
    }

    sort::BubbleSort(arr); sort::SelectionSort(arr2); sort::InsertionSort(arr3);

    PrintArr(arr); PrintArr(arr2); PrintArr(arr3);

    return 0;
}