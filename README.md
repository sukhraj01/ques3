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

Notes and behavior

- The `main.py` script now automatically creates a `reports/` directory next to itself and writes
	results to `reports/output.txt` (one result or message per input line). You don't need to redirect
	output unless you prefer a different location.

- For safety/performance, if a line requests `bubble` or `selection` on a large input (size &gt; 10000),
	the program will automatically switch to `merge` (and will write a warning in the report). This
	prevents very long-running O(n^2) sorts on large inputs. If you want to force a particular
	algorithm regardless of size, run the sorting logic from the classes directly.

- Input parsing is more robust: malformed integers or mismatched size values are reported per-line in
	the report file instead of causing an uncaught exception.

Git usage (assignment requirement)

This repository must be tracked with git for the assignment. Example workflow (run from the project root):

```bash
git add Q3
git commit -m "Implement sorting package, tests, and report writing"
git tag -a sorting_submission_v1 -m "Submission v1"
# Optionally push to a remote if you use one:
git push --follow-tags origin main
```

Make sure to create a branch or tag as required by your instructor. I didn't modify git metadata in this
workspace automatically; perform the commits/tags locally when you're ready.
