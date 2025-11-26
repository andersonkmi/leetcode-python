#!/usr/bin/env python3
import sys
from wc.wordcounter import count_bytes

def main():
    if len(sys.argv) < 3:
        print("Usage: ccwc.py <option> <file>")
        print("Options: -c, -l, -w, -m")
        sys.exit(1)

    option = sys.argv[1]
    file_name = sys.argv[2]

    try:
        match option:
            case "-c":
                print_file_size_in_bytes(file_name)
            case "-l":
                print("Option -l selected")
            case "-w":
                print("Option -w selected")
            case "-m":
                print("Option -m selected")
            case _:
                print("Option {} is invalid".format(option))
                sys.exit(1)
    except FileNotFoundError:
        print("{} file does not exist".format(file_name))
        sys.exit(2)

    sys.exit(0)

def print_file_size_in_bytes(file_name):
    size_bytes = count_bytes(file_name)
    print("{} {}".format(size_bytes, file_name))


if __name__ == "__main__":
    main()