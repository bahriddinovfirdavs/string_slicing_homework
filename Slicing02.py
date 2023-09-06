def main(s):
    """
    The s string variable is given. return four characters from the end.
    Args:
        s(str): parameter
    Returns:
        str: answer
    """
    r=s[-4:-1:1]
    q=s[-1]
    return r+q
