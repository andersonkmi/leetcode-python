def count_bytes(file_name):
    with open(file_name, encoding="utf-8") as file:
        file.seek(0, 2)
        size_bytes = file.tell()
        return size_bytes

def count_lines(file_name):
    lines = []
    with open(file_name, encoding="utf-8") as file:
        for line in file:
            lines.append(line)

    return len(lines)

def count_words(file_name):
    words = []
    with open(file_name, encoding="utf-8") as file:
        for line in file:
            split_words = line.split()
            for word in split_words:
                words.append(word)

    return len(words)