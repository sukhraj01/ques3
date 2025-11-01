import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from bubble_sort import BubbleSort
from selection_sort import SelectionSort
from quick_sort import QuickSort
from merge_sort import MergeSort


def test_bubble_sort_ascending():
    bs = BubbleSort()
    arr = [64, 34, 25, 12, 22, 11, 90]
    expected = [11, 12, 22, 25, 34, 64, 90]
    result = bs.sort(arr, ascending=True)
    assert result == expected, f"Expected {expected}, got {result}"


def test_bubble_sort_descending():
    bs = BubbleSort()
    arr = [64, 34, 25, 12, 22, 11, 90]
    expected = [90, 64, 34, 25, 22, 12, 11]
    result = bs.sort(arr, ascending=False)
    assert result == expected, f"Expected {expected}, got {result}"


def test_selection_sort_ascending():
    ss = SelectionSort()
    arr = [64, 34, 25, 12, 22, 11, 90]
    expected = [11, 12, 22, 25, 34, 64, 90]
    result = ss.sort(arr, ascending=True)
    assert result == expected, f"Expected {expected}, got {result}"


def test_selection_sort_descending():
    ss = SelectionSort()
    arr = [64, 34, 25, 12, 22, 11, 90]
    expected = [90, 64, 34, 25, 22, 12, 11]
    result = ss.sort(arr, ascending=False)
    assert result == expected, f"Expected {expected}, got {result}"


def test_quick_sort_ascending():
    qs = QuickSort()
    arr = [64, 34, 25, 12, 22, 11, 90]
    expected = [11, 12, 22, 25, 34, 64, 90]
    result = qs.sort(arr, ascending=True)
    assert result == expected, f"Expected {expected}, got {result}"


def test_quick_sort_descending():
    qs = QuickSort()
    arr = [64, 34, 25, 12, 22, 11, 90]
    expected = [90, 64, 34, 25, 22, 12, 11]
    result = qs.sort(arr, ascending=False)
    assert result == expected, f"Expected {expected}, got {result}"


def test_merge_sort_ascending():
    ms = MergeSort()
    arr = [64, 34, 25, 12, 22, 11, 90]
    expected = [11, 12, 22, 25, 34, 64, 90]
    result = ms.sort(arr, ascending=True)
    assert result == expected, f"Expected {expected}, got {result}"


def test_merge_sort_descending():
    ms = MergeSort()
    arr = [64, 34, 25, 12, 22, 11, 90]
    expected = [90, 64, 34, 25, 22, 12, 11]
    result = ms.sort(arr, ascending=False)
    assert result == expected, f"Expected {expected}, got {result}"


def test_empty_list():
    bs = BubbleSort()
    arr = []
    expected = []
    result = bs.sort(arr, ascending=True)
    assert result == expected, f"Expected {expected}, got {result}"


def test_single_element():
    bs = BubbleSort()
    arr = [42]
    expected = [42]
    result = bs.sort(arr, ascending=True)
    assert result == expected, f"Expected {expected}, got {result}"


def test_negative_numbers():
    ms = MergeSort()
    arr = [-5, 3, -1, 7, -8, 0]
    expected = [-8, -5, -1, 0, 3, 7]
    result = ms.sort(arr, ascending=True)
    assert result == expected, f"Expected {expected}, got {result}"


def test_duplicate_elements():
    qs = QuickSort()
    arr = [5, 2, 8, 2, 9, 1, 5]
    expected = [1, 2, 2, 5, 5, 8, 9]
    result = qs.sort(arr, ascending=True)
    assert result == expected, f"Expected {expected}, got {result}"


def run_all_tests():
    tests = [
        test_bubble_sort_ascending,
        test_bubble_sort_descending,
        test_selection_sort_ascending,
        test_selection_sort_descending,
        test_quick_sort_ascending,
        test_quick_sort_descending,
        test_merge_sort_ascending,
        test_merge_sort_descending,
        test_empty_list,
        test_single_element,
        test_negative_numbers,
        test_duplicate_elements
    ]

    passed = 0
    failed = 0

    for test in tests:
        try:
            test()
            print(f"PASSED: {test.__name__}")
            passed += 1
        except AssertionError as e:
            print(f"FAILED: {test.__name__} - {e}")
            failed += 1
        except Exception as e:
            print(f"ERROR: {test.__name__} - {e}")
            failed += 1

    print(f"\n{passed} tests passed, {failed} tests failed")
    return failed == 0


if __name__ == "__main__":
    success = run_all_tests()
    sys.exit(0 if success else 1)
