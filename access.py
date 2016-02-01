def answer(x):
    """
    Given list of codes consisting of chars a-z, determine number of unique codes.
    Codes can be read forward or backward, so abc == cba.
    """

    unique_codes = set()

    for code in x:
        if code in unique_codes or code[::-1] in unique_codes:
            continue
        else:
            unique_codes.add(code)

    return len(unique_codes)
