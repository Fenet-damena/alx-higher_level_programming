#!/user/bin/python3
"""defines function that add number"""
def add_integer(a, b=98):
    """ return sum of two number if they are integer
    or 
    Raises: 
    TypeError:if they are not integer"""
    if ((not isinstance(a, int) and not instance(a, float))):
        raise TypeError("a must be integer")
    if ((not isinstance(b, int) and not isinstance(a, float))):
        raise TypeError("b must be integer")
    return (int(a) + int(b))
