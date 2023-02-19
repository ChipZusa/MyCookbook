#! /usr/bin/env python3
"""Created by chris at 2/18/23


Ref: 
"""
# Custom exception template
class CustomError(Exception):
    """the template for a custom exeption"""

    # pylint: disable=unnecessary-pass

    ...
    pass

# end then this code goes in your script
def some_code_snippet():
    """sample snippet that raises an exception"""

    try:
        ...
    except CustomError:
        ...

# Following is an example with an EmptyStackError exception
# my EmptyStackError class
class EmptyStackError(Exception):  # also do with IndexError parent
    """Notify when an empty stack is being accessed."""

    # pylint: disable=unnecessary-pass


# end then this code goes in your script
def error_example_fun():
    """sample snippet that raises an exception
    >>> alist = list("123")
    >>> alist
    ['1', '2', '3']
    >>> num = alist[0]
    >>> num
    '1'
    >>> num = alist[3]
    Traceback (most recent call last):
    ...
    IndexError: list index out of range
    >>> raise EmptyStackError
    Traceback (most recent call last):
    ...
    EmptyStackError

    """
    # alist = list("123")
    alist = []

    try:
        if len(alist) < 1:
            raise EmptyStackError("Length of alist is zero")

        num = alist[1]
    except EmptyStackError as err:
        print(f"Message from the raise: {err}")
        print("In except EmptyStackError ... and")
        print("additional handler business goes here.")
    except IndexError:
        print("in IndexError except")
        # raise EmptyStackError("in the IndexError except")
    else:
        print("in the try-else clause")





if __name__ == "__main__":
    import doctest

    doctest.testmod()
    error_example_fun()


