#include <iostream>
#include <vector>
#include <algorithm>

int binary_search(std::vector<int>& arr, int target) {
    int left = 0;
    int right = arr.size() - 1;

    while (left <= right) {
        int mid = (left + right) / 2;
        if (arr[mid] == target) {
            return mid;
        }

        if (arr[mid] > target)
            right = mid - 1;
        else
            left = mid + 1;
    }

    return -1;
}

int lower_bound(std::vector<int>& arr, int target) {
    int size = arr.size();
    int left = 0;
    int right = size - 1;
    int min_idx = size;

    while (left <= right) {
        int mid = (left + right) / 2;
        if (arr[mid] >= target) {
            right = mid - 1;
            min_idx = std::min(min_idx, mid);
        } else {
            left = mid + 1;
        }
    }

    return min_idx;
}

int upper_bound(std::vector<int> & arr, int target) {
    int left = 0;
    int right = arr.size() - 1;
    int max_idx = -1;

    while (left <= right) {
        int mid = (left + right) / 2;
        if (arr[mid] > target) {
            right = mid - 1;
            max_idx = std::max(max_idx, mid);
        } else {
            left = mid + 1;
        }
    }

    return max_idx;
}

int custom_bound(std::vector<int>& arr, int target) {
    int left = 0;
    int right = arr.size() -1;
    int max_idx = -1;
    
    while (left <= right) {
        int mid = (left + right) / 2;
        if (arr[mid] > target) {
            right = mid - 1;
        } else {
            left = mid + 1;
            max_idx = std::max(max_idx, mid);
        }
    }
    
    return max_idx;
}

int main() {
    std::vector<int> arr = {23, 34, 36, 41, 45, 49, 52, 57, 64, 72, 76, 81, 89};
    std::vector<int> arr2 = {23, 34, 36, 45, 45, 45, 52, 57, 64, 72, 76, 81, 89};

    int idx = binary_search(arr, 45);
    int min_idx = lower_bound(arr2, 45);
    int upper_idx = upper_bound(arr2, 45);
    int max_idx = custom_bound(arr2, 45);

    std::cout << idx << "\n";
    std::cout << min_idx << "\n";
    std::cout << upper_idx << "\n";
    std::cout << upper_idx - min_idx << "\n";
    std::cout << max_idx << "\n";
    
    return 0;
}