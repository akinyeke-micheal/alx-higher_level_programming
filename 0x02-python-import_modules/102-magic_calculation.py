def magic_calculation(a, b):

    from magic_calculation_102 import add, sub

    if a < b:
        c = add(a, b)
        for i in range(4, 6):
            c = add(c, i)
        return c  # Removed the unnecessary parentheses

    else:
        return sub(a, b)  # Use the add function for the else branchin
