def count_bytes(file_name):
    with open(file_name, encoding="utf-8") as file:
        file.seek(0, 2)
        size_bytes = file.tell()
        return size_bytes

def count_lines(file_name):
    with open(file_name, encoding="utf-8") as file:
        lines = []
        for line in file:
            lines.append(line)

        return len(lines)