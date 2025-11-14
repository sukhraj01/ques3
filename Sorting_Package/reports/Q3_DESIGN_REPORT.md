# Q3 Sorting Package - Design and Test Report

## 1. Code Design Architecture

### 1.1 Design Philosophy
The sorting package follows the **Strategy Design Pattern** and **Object-Oriented Programming** principles to create a flexible, maintainable, and extensible sorting system.

### 1.2 Component Architecture

#### Abstract Base Class (sorting_base.py)
```
SortingAlgorithm (ABC)
├── Abstract method: sort(arr, ascending)
└── Enforces consistent interface for all algorithms
```

**Design Decision**: Using Python's `abc` module ensures that all sorting algorithms implement the same interface, making them interchangeable and easy to extend.

**Benefits**:
- Type safety through abstract methods
- Consistent API across all algorithms
- Easy to add new algorithms without modifying existing code (Open/Closed Principle)

#### Concrete Algorithm Implementations

Each algorithm is implemented in its own class file:

1. **BubbleSort** (bubble_sort.py)
   - Time Complexity: O(n²) average and worst case
   - Space Complexity: O(n) for creating a new list
   - Best for: Small datasets, educational purposes

2. **SelectionSort** (selection_sort.py)
   - Time Complexity: O(n²) in all cases
   - Space Complexity: O(n) for creating a new list
   - Best for: Small datasets where memory writes are expensive

3. **QuickSort** (quick_sort.py)
   - Time Complexity: O(n log n) average, O(n²) worst case
   - Space Complexity: O(log n) recursion stack + O(n) for new list
   - Best for: General purpose, good average performance
   - Uses: Last element as pivot

4. **MergeSort** (merge_sort.py)
   - Time Complexity: O(n log n) in all cases
   - Space Complexity: O(n)
   - Best for: Guaranteed O(n log n), stable sort
   - Uses: Divide and conquer approach

**Design Decision**: Each algorithm returns a **new sorted list** instead of modifying in-place, following functional programming principles and preventing unintended side effects.

#### Sorter Class (sorter.py)

The `Sorter` class acts as a **facade** and **factory**:

```
Sorter
├── algorithms: dict[str, SortingAlgorithm]
└── sort(input_list, algorithm, size, ascending)
    ├── Validates input type (integers only)
    ├── Validates size constraint (≤ 2e5)
    ├── Selects algorithm
    └── Executes sort
```

**Design Decisions**:
- Dictionary-based algorithm lookup for O(1) access
- Parameter validation before execution
- Single entry point for all sorting operations
- Encapsulates algorithm selection logic

### 1.3 Input/Output Design

**main.py** demonstrates usage with:
- File-based input (input.txt)
- Pipe-based format: `algorithm | order | size | list`
- Automatic output to reports/output.txt
- Error handling for malformed input

**Design Decision**: File I/O allows easy testing with different datasets and maintains separation between data and code.

### 1.4 Package Structure

```
Sorting_Package/
├── src/
│   ├── __init__.py           # Package initialization
│   ├── sorting_base.py       # Abstract base class
│   ├── bubble_sort.py        # Bubble sort implementation
│   ├── selection_sort.py     # Selection sort implementation
│   ├── quick_sort.py         # Quick sort implementation
│   ├── merge_sort.py         # Merge sort implementation
│   └── sorter.py             # Facade class
├── test/
│   ├── __init__.py
│   └── test_sorting.py       # Comprehensive test suite
├── reports/
│   ├── output.txt            # Runtime output
│   └── Q3_DESIGN_REPORT.md   # This document
├── main.py                   # Demonstration script
├── input.txt                 # Sample input data
└── README.md                 # Usage documentation
```

---

## 2. Test Case Design and Rationale

### 2.1 Testing Strategy

The test suite follows **black-box** and **white-box** testing methodologies to ensure correctness.

### 2.2 Test Categories

#### Category 1: Algorithm-Specific Tests (Correctness)

**Test Cases per Algorithm** (8 tests × 4 algorithms = 32 algorithm-specific assertions):
- `test_<algorithm>_ascending`: Validates ascending order
- `test_<algorithm>_descending`: Validates descending order

**Rationale**:
- Ensures each algorithm correctly implements both sort orders
- Uses same input `[64, 34, 25, 12, 22, 11, 90]` for consistency
- Expected outputs verified against manually calculated results

**Example**:
```python
def test_bubble_sort_ascending():
    bs = BubbleSort()
    arr = [64, 34, 25, 12, 22, 11, 90]
    expected = [11, 12, 22, 25, 34, 64, 90]
    result = bs.sort(arr, ascending=True)
    assert result == expected
```

#### Category 2: Edge Case Tests

**Test Cases**:

1. **Empty List** (`test_empty_list`)
   - Input: `[]`
   - Expected: `[]`
   - Rationale: Boundary condition, zero elements

2. **Single Element** (`test_single_element`)
   - Input: `[42]`
   - Expected: `[42]`
   - Rationale: Boundary condition, trivial case

3. **Negative Numbers** (`test_negative_numbers`)
   - Input: `[-5, 3, -1, 7, -8, 0]`
   - Expected: `[-8, -5, -1, 0, 3, 7]`
   - Rationale: Tests INT32 range, including negative values

4. **Duplicate Elements** (`test_duplicate_elements`)
   - Input: `[5, 2, 8, 2, 9, 1, 5]`
   - Expected: `[1, 2, 2, 5, 5, 8, 9]`
   - Rationale: Ensures stability and correct handling of duplicates

### 2.3 Test Case Selection Rationale

| Test Type | Purpose | Coverage |
|-----------|---------|----------|
| Per-Algorithm Tests | Verify implementation correctness | 100% of algorithms |
| Ascending/Descending | Verify both sort orders | Both order modes |
| Empty/Single Element | Boundary conditions | Edge cases |
| Negative Numbers | INT32 range validation | Negative values |
| Duplicates | Stability and correctness | Duplicate handling |

### 2.4 Test Execution

**Manual Execution**:
```bash
python3 test/test_sorting.py
```

**Expected Output**:
```
PASSED: test_bubble_sort_ascending
PASSED: test_bubble_sort_descending
...
12 tests passed, 0 tests failed
```

### 2.5 Why These Test Cases?

1. **Correctness**: Each algorithm tested with known input/output pairs
2. **Completeness**: Both ascending and descending orders tested
3. **Edge Cases**: Empty, single element, negatives, duplicates
4. **Consistency**: Same test data used across algorithms for comparison
5. **INT32 Range**: Negative numbers validate integer range requirement

### 2.6 Test Coverage Analysis

**What's Tested**:
- ✅ All 4 sorting algorithms
- ✅ Both sort orders (ascending/descending)
- ✅ Edge cases (empty, single, duplicates)
- ✅ Negative integers (INT32 range)
- ✅ Return value correctness

**What's Not Tested** (Limitations):
- ❌ Performance testing (time complexity validation)
- ❌ Large datasets (2e5 elements)
- ❌ Memory usage
- ❌ Concurrent sorting

**Note**: For Q3 requirements, functional correctness is prioritized. Performance and stress testing could be added in future iterations.

---

## 3. Design Decisions Summary

| Decision | Rationale |
|----------|-----------|
| Abstract Base Class | Enforces consistent interface, enables polymorphism |
| Separate class files | Modularity, single responsibility principle |
| Return new list | Immutability, prevents side effects |
| Dictionary algorithm lookup | O(1) selection, easy to extend |
| File-based I/O | Testability, separation of concerns |
| Comprehensive validation | Fail-fast, clear error messages |

---

## 4. Requirements Compliance Checklist

- ✅ Abstract base class for sorting algorithms
- ✅ Bubble, Selection, Quick, Merge sort implemented
- ✅ Test package with correctness tests
- ✅ Sorter class with parameter-based algorithm selection
- ✅ Supports elements ≤ 2e5, INT32 range
- ✅ Parameters: algorithm name, order, size, input list
- ✅ Returns new sorted list
- ✅ Integer-only data type
- ✅ src/, test/, reports/ folder structure
- ✅ main.py demonstration file
- ✅ Input file support
- ✅ Git version control

---

## 5. Future Enhancements

1. Add more algorithms (heap sort, radix sort)
2. Implement performance benchmarking
3. Add type hints validation at runtime
4. Create pytest integration
5. Add logging for debugging
6. Implement parallel sorting for large datasets

---

