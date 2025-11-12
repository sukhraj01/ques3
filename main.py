import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from src.sorter import Sorter


def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <input_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    # Ensure reports directory exists and prepare output file
    reports_dir = os.path.join(os.path.dirname(__file__), 'reports')
    os.makedirs(reports_dir, exist_ok=True)
    output_file_path = os.path.join(reports_dir, 'output.txt')

    try:
        with open(input_file, 'r') as f:
            lines = f.readlines()

        sorter = Sorter()

        # Open the output file and write each result there (one per line)
        with open(output_file_path, 'w') as out_f:
            for line in lines:
                raw = line.strip()
                if not raw:
                    continue

                parts = raw.split('|')
                if len(parts) != 4:
                    # Log invalid input format to the output file
                    out_f.write(f"Invalid input format: {raw}\n")
                    continue

                # Parse and validate parameters
                algorithm = parts[0].strip().lower()
                order = parts[1].strip()

                # size: validate integer
                try:
                    size = int(parts[2].strip())
                except ValueError:
                    out_f.write(f"Invalid size value in line: {raw}\n")
                    continue

                # Parse input list with robust per-token validation
                raw_tokens = [tok.strip() for tok in parts[3].strip().split(',') if tok.strip() != '']
                input_list = []
                parse_error = False
                for tok in raw_tokens:
                    try:
                        # enforce integer-only values
                        val = int(tok)
                        input_list.append(val)
                    except ValueError:
                        out_f.write(f"Invalid integer '{tok}' in line: {raw}\n")
                        parse_error = True
                        break

                if parse_error:
                    continue

                # Check reported size vs actual parsed list
                if len(input_list) != size:
                    out_f.write(f"Size parameter does not match number of elements in line: {raw}\n")
                    continue

                ascending = order.lower() == 'ascending'

                # Safety: avoid running O(n^2) sorts on very large inputs. If user requests
                # bubble/selection for large n, automatically switch to merge to guarantee completion.
                auto_switched = False
                if algorithm in ('bubble', 'selection') and size > 10000:
                    out_f.write(f"Warning: algorithm '{algorithm}' is O(n^2) and may be too slow for size={size}.\n")
                    out_f.write(f"Auto-switching to 'merge' for this input to ensure completion.\n")
                    algorithm = 'merge'
                    auto_switched = True

                if algorithm not in sorter.algorithms:
                    out_f.write(f"Unknown algorithm: {algorithm} in line: {raw}. Choose from: {list(sorter.algorithms.keys())}\n")
                    continue

                try:
                    result = sorter.sort(input_list, algorithm, size, ascending)
                    # Write auto-switch info once before the result if it happened
                    if auto_switched:
                        out_f.write(f"Result (auto-used merge): {str(result)}\n")
                    else:
                        out_f.write(str(result) + "\n")
                except Exception as e:
                    # Write per-line errors to the output file for easier debugging
                    out_f.write(f"Error processing line '{raw}': {e}\n")

    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
