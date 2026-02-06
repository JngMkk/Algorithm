#ifndef SORT_H
#define SORT_H

#include <vector>

namespace sort {

void BubbleSort(std::vector<int>& arr) noexcept;
void SelectionSort(std::vector<int>& arr) noexcept;
void InsertionSort(std::vector<int>& arr) noexcept;

} // namespace sort

#endif