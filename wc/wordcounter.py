def count_bytes(file_name):
    with open(file_name, encoding="utf-8") as file:
        file.seek(0, 2)
        size_bytes = file.tell()
        return size_bytes