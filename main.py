import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from src.sorter import Sorter


def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <input_file>")
        sys.exit(1)

    input_file = sys.argv[1]

    try:
        with open(input_file, 'r') as f:
            lines = f.readlines()

        sorter = Sorter()

        for line in lines:
            line = line.strip()
            if not line:
                continue

            parts = line.split('|')
            if len(parts) != 4:
                print(f"Invalid input format: {line}")
                continue

            algorithm = parts[0].strip()
            order = parts[1].strip()
            size = int(parts[2].strip())
            input_list = list(map(int, parts[3].strip().split(',')))

            ascending = order.lower() == 'ascending'

            result = sorter.sort(input_list, algorithm, size, ascending)
            print(result)

    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
