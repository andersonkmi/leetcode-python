#!/usr/bin/env python3
import sys
from wc.wordcounter import count_bytes, count_lines, count_words, count_chars

OPTION_AND_FILE_ARGS_LENGTH = 3
FILE_ARG_LENGTH = 2

def main():
    if len(sys.argv) == OPTION_AND_FILE_ARGS_LENGTH:
        option = sys.argv[1]
        file_name = sys.argv[2]
        try:
            match option:
                case "-c":
                    print_file_size_in_bytes(file_name)
                case "-l":
                    print_number_lines(file_name)
                case "-w":
                    print_total_words(file_name)
                case "-m":
                    print_total_chars(file_name)
        except FileNotFoundError:
            print("{} file does not exist".format(file_name))
            sys.exit(2)
    elif len(sys.argv) == FILE_ARG_LENGTH:
        file_name = sys.argv[1]
        print_total_size_lines_chars(file_name)


def print_file_size_in_bytes(file_name):
    size_bytes = count_bytes(file_name)
    print("{} {}".format(size_bytes, file_name))

def print_number_lines(file_name):
    number_lines = count_lines(file_name)
    print("{} {}".format(number_lines, file_name))

def print_total_words(file_name):
    number_words = count_words(file_name)
    print("{} {}".format(number_words, file_name))

def print_total_chars(file_name):
    number_chars = count_chars(file_name)
    print("{} {}".format(number_chars, file_name))

def print_total_size_lines_chars(file_name):
    size_bytes = count_bytes(file_name)
    number_lines = count_lines(file_name)
    number_words = count_words(file_name)
    print("{} {} {} {}".format(number_lines, number_words, size_bytes, file_name))

if __name__ == "__main__":
    main()