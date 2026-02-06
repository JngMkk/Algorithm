#include "sort.h"

#include <algorithm>

namespace sort {

void BubbleSort(std::vector<int>& arr) noexcept {
    int len = arr.size();

    for (int i = 0; i + 1 < len; ++i) {
        for (int j = 0; j + 1 < len - i; ++j) {
            if (arr[j] > arr[j + 1])
                std::swap(arr[j], arr[j + 1]);
        }
    }
}

void SelectionSort(std::vector<int>& arr) noexcept {
    int len = arr.size();

    for (int i = 0; i + 1 < len; ++i) {
        int min = i;
        for (int j = i + 1; j < len; ++j) {
            if (arr[j] < arr[min])
                min = j;
        }
        std::swap(arr[i], arr[min]);
    }
}

void InsertionSort(std::vector<int>& arr) noexcept {
    int len = arr.size();

    for (int i = 1; i < len; ++i) {
        int j = i - 1;
        int key = arr[i];
        while (j >= 0 && arr[j] > key) {
            arr[j + 1] = arr[j];
            j--;
        }

        arr[j + 1] = key;
    }
}

}