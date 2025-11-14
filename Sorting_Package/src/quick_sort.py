from typing import List
try:
    from .sorting_base import SortingAlgorithm
except ImportError:
    from sorting_base import SortingAlgorithm


class QuickSort(SortingAlgorithm):
    """Quick sort implementation."""

    def sort(self, arr: List[int], ascending: bool = True) -> List[int]:
        """
        Sort the input array using quick sort.

        Args:
            arr: List of integers to sort
            ascending: True for ascending order, False for descending

        Returns:
            New sorted list
        """
        result = arr.copy()
        self._quick_sort(result, 0, len(result) - 1, ascending)
        return result

    def _quick_sort(self, arr: List[int], low: int, high: int, ascending: bool):
        """Helper function for quick sort."""
        if low < high:
            pi = self._partition(arr, low, high, ascending)
            self._quick_sort(arr, low, pi - 1, ascending)
            self._quick_sort(arr, pi + 1, high, ascending)

    def _partition(self, arr: List[int], low: int, high: int, ascending: bool) -> int:
        """Partition function for quick sort."""
        pivot = arr[high]
        i = low - 1

        for j in range(low, high):
            if ascending:
                if arr[j] <= pivot:
                    i += 1
                    arr[i], arr[j] = arr[j], arr[i]
            else:
                if arr[j] >= pivot:
                    i += 1
                    arr[i], arr[j] = arr[j], arr[i]

        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1
