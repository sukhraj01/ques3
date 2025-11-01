from typing import List
from .bubble_sort import BubbleSort
from .selection_sort import SelectionSort
from .quick_sort import QuickSort
from .merge_sort import MergeSort


class Sorter:
    """Class to call various sorting algorithms based on parameter."""

    def __init__(self):
        self.algorithms = {
            'bubble': BubbleSort(),
            'selection': SelectionSort(),
            'quick': QuickSort(),
            'merge': MergeSort()
        }

    def sort(self, input_list: List[int], algorithm: str, size: int, ascending: bool = True) -> List[int]:
        """
        Sort the input list using the specified algorithm.

        Args:
            input_list: List of integers to sort
            algorithm: Name of the algorithm ('bubble', 'selection', 'quick', 'merge')
            size: Size of the list
            ascending: True for ascending order, False for descending

        Returns:
            New sorted list

        Raises:
            ValueError: If algorithm name is invalid or input validation fails
        """
        if not all(isinstance(x, int) for x in input_list):
            raise ValueError("All elements must be integers")

        if len(input_list) != size:
            raise ValueError("Size parameter does not match input list length")

        if size > 2e5:
            raise ValueError("Size must be less than 2e5")

        if algorithm not in self.algorithms:
            raise ValueError(f"Unknown algorithm: {algorithm}. Choose from: {list(self.algorithms.keys())}")

        return self.algorithms[algorithm].sort(input_list, ascending)
