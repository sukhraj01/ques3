# Sorting Package

A Python package implementing various sorting algorithms with a unified interface.

## Structure

```
Sorting_Package/
├── src/              # Source code
├── test/             # Test package
├── reports/          # Output reports
├── main.py           # Main demonstration file
└── input.txt         # Sample input file
```

## Algorithms Implemented

1. Bubble Sort
2. Selection Sort
3. Quick Sort
4. Merge Sort

## Usage

### Running with Input File

```bash
python3 main.py input.txt
```

### Redirecting Output

```bash
python3 main.py input.txt > reports/output.txt
```

### Input File Format

Each line should follow this format:
```
algorithm | order | size | comma-separated-list
```

Example:
```
bubble | ascending | 7 | 64,34,25,12,22,11,90
selection | descending | 7 | 64,34,25,12,22,11,90
quick | ascending | 10 | 3,7,8,5,2,1,9,5,4,6
merge | descending | 6 | -5,3,-1,7,-8,0
```

### Running Tests

```bash
python3 test/test_sorting.py
```

## Constraints

- Elements must be integers (INT32 range)
- Maximum size: 2x10^5 elements
- Algorithms: bubble, selection, quick, merge
- Order: ascending or descending
