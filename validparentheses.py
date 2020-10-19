def is_valid(input: str):
    if not input:
        return True
    elif len(input) % 2 == 1:
        return False
    return True