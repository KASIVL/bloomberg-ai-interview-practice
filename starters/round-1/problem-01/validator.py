def is_valid_access_code(code):
    """Return whether code is a valid six digit student access code."""
    try:
        return len(str(int(code))) == 6
    except (TypeError, ValueError):
        return False
