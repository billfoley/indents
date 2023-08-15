def count_indents(text: str) -> int:
    """
    Count and return the number of leading white space characters (' ').
    """
    count = 0

    for i in text:
        if i != " ":
            break
        else:
            count += 1

    return count
