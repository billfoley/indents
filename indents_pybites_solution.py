def count_indents(text: str) -> int:
    """
    Count and return the number of leading white space characters (' ').
    """
    # originally we had:
    # import re
    # re.split('\S', s)[0].count(' ')
    # but this is more elegant (credit: https://stackoverflow.com/a/13241465)
    return len(text) - len(text.lstrip(' '))
