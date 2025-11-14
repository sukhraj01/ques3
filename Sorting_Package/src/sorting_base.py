from abc import ABC, abstractmethod
from typing import List


class SortingAlgorithm(ABC):
    """Abstract base class for sorting algorithms."""

    @abstractmethod
    def sort(self, arr: List[int], ascending: bool = True) -> List[int]:
        """
        Sort the input array.

        Args:
            arr: List of integers to sort
            ascending: True for ascending order, False for descending

        Returns:
            New sorted list
        """
        pass
