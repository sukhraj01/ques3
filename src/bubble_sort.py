from typing import List
try:
    from .sorting_base import SortingAlgorithm
except ImportError:
    from sorting_base import SortingAlgorithm


class BubbleSort(SortingAlgorithm):
    """Bubble sort implementation."""

    def sort(self, arr: List[int], ascending: bool = True) -> List[int]:
        """
        Sort the input array using bubble sort.

        Args:
            arr: List of integers to sort
            ascending: True for ascending order, False for descending

        Returns:
            New sorted list
        """
        result = arr.copy()
        n = len(result)

        for i in range(n):
            for j in range(0, n - i - 1):
                if ascending:
                    if result[j] > result[j + 1]:
                        result[j], result[j + 1] = result[j + 1], result[j]
                else:
                    if result[j] < result[j + 1]:
                        result[j], result[j + 1] = result[j + 1], result[j]

        return result
