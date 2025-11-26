#!/usr/bin/env python3
import sys

def main():
    if len(sys.argv) < 3:
        print("Usage: ccwc.py <option> <file>")
        print("Options: -c, -l, -w, -m")
        sys.exit(1)

    option = sys.argv[1]
    file_name = sys.argv[2]

    match option:
        case "-c":
            print("Option -c selected")
        case "-l":
            print("Option -l selected")
        case "-w":
            print("Option -w selected")
        case "-m":
            print("Option -m selected")
        case _:
            print("Option {} is invalid".format(option))
            sys.exit(1)

    sys.exit(0)

if __name__ == "__main__":
    main()