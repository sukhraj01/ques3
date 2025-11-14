from typing import List
try:
    from .sorting_base import SortingAlgorithm
except ImportError:
    from sorting_base import SortingAlgorithm


class MergeSort(SortingAlgorithm):
    """Merge sort implementation."""

    def sort(self, arr: List[int], ascending: bool = True) -> List[int]:
        """
        Sort the input array using merge sort.

        Args:
            arr: List of integers to sort
            ascending: True for ascending order, False for descending

        Returns:
            New sorted list
        """
        result = arr.copy()
        self._merge_sort(result, 0, len(result) - 1, ascending)
        return result

    def _merge_sort(self, arr: List[int], left: int, right: int, ascending: bool):
        """Helper function for merge sort."""
        if left < right:
            mid = (left + right) // 2
            self._merge_sort(arr, left, mid, ascending)
            self._merge_sort(arr, mid + 1, right, ascending)
            self._merge(arr, left, mid, right, ascending)

    def _merge(self, arr: List[int], left: int, mid: int, right: int, ascending: bool):
        """Merge function for merge sort."""
        left_part = arr[left:mid + 1]
        right_part = arr[mid + 1:right + 1]

        i = j = 0
        k = left

        while i < len(left_part) and j < len(right_part):
            if ascending:
                if left_part[i] <= right_part[j]:
                    arr[k] = left_part[i]
                    i += 1
                else:
                    arr[k] = right_part[j]
                    j += 1
            else:
                if left_part[i] >= right_part[j]:
                    arr[k] = left_part[i]
                    i += 1
                else:
                    arr[k] = right_part[j]
                    j += 1
            k += 1

        while i < len(left_part):
            arr[k] = left_part[i]
            i += 1
            k += 1

        while j < len(right_part):
            arr[k] = right_part[j]
            j += 1
            k += 1
