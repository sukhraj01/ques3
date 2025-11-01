from typing import List
from .sorting_base import SortingAlgorithm


class SelectionSort(SortingAlgorithm):
    """Selection sort implementation."""

    def sort(self, arr: List[int], ascending: bool = True) -> List[int]:
        """
        Sort the input array using selection sort.

        Args:
            arr: List of integers to sort
            ascending: True for ascending order, False for descending

        Returns:
            New sorted list
        """
        result = arr.copy()
        n = len(result)

        for i in range(n):
            idx = i
            for j in range(i + 1, n):
                if ascending:
                    if result[j] < result[idx]:
                        idx = j
                else:
                    if result[j] > result[idx]:
                        idx = j

            result[i], result[idx] = result[idx], result[i]

        return result
