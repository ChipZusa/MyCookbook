#! /usr/bin/env python3
"""Created by chris at 1/22/23

Examples of:
    field_name
    format_width_and_padding
    format_with_precision
    format_percentage
    format_scientific_notation

Ref: file:///home/chris/Documents/Documentation/Python/python-3.8.13-docs-html/library/string.html?highlight=string%20format#format-string-syntax
"""
# pylint: disable=consider-using-f-string
# Field name
def field_names():
    """Demonstration of field names in strings."""
    # pylint: disable=C0209
    the_string = "This is the {} name".format("field")
    print(the_string)  # f-strings are more practical for these examples
    the_string = "This is the {} and {} field names".format("first", "second")
    print(the_string)
    the_string = "This is the {1} and {0} field names".format("first", "second")
    print(the_string)

    # Using f-strings
    print()
    f_string = f"This is the {'first'} field."
    print(f_string)
    field1 = "one"
    field2 = 2
    f_string = f"this is field {field1} and this is {field2}."
    print(f_string)


def format_width_and_padding():
    """Examples of using formats of width, alignment, padding, and precision.
    Note: all formats follow a colon (":")."""
    # A leading ':' indicates a format is coming.
    # minimum total field width uses a decimal integer
    the_string = "The first column {:10} and then {:10}.".format("here", 100.00)
    print(the_string)

    # Excess width can be filled with a character.
    # The character is followed by the alignment indicator
    the_string = "The first column {0:!<10} and then {1:0<10} or {1:0>10}.".format(
        "here", 100.00
    )
    print(the_string)

    # Alignments can be:
    # left
    the_string = "Aligned {:<10} and {:>10} like this.".format("left", "right")
    print(the_string)

    # Padding between the sign and digits
    the_string = "Padding between the sign and digits: {:=10}.".format(-23)
    print(the_string)
    # Force the filed to be centered.
    the_string = "This {:^15} is centered.".format("field")
    print(the_string)


def format_with_precision():
    """Examples of formatting precision.
    Note: all formats follow a colon (":") and precision follows a period (".").
        Precision gives digits after decimal points for "f" and "F" types"""
    the_string = "This has {:.2f} places {:.2f}.".format(2.0, 22.23663)
    print(the_string)
    the_string = "Total number of digits with non-f types: {0:.4} and {0:10.2}.".format(
        23.5553
    )
    print(the_string)


def format_percentage():
    """Example of formating a percetage"""
    the_string = "This is {0:%} or {0:.0%}.".format(0.1)
    print(the_string)


def format_scientific_notation():
    """Examples of scientific notation"""
    the_string = "The value: {0:e} or {0:.3e}.".format(4533.01)
    print(the_string)
    the_string = "The value: {0:e} or {0:.3e}.".format(3.01566633)
    print(the_string)
    the_string = "The value: {0:e} or {0:.3e}.".format(75483757592.01)
    print(the_string)
    print()

    # And let's try using "g" or "G" (save exponential until requried)
    the_string = "The value: {0:g} or {0:.3g}.".format(4533.01)
    print(the_string)
    the_string = "The value: {0:g} or {0:.3g}.".format(3.01566633)
    print(the_string)
    the_string = "The value: {0:g} or {0:.3g}.".format(75483757592.01)
    print(the_string)

def format_bases():
    """Use formatting to other base representations"""
    x_dec = 23  # '0b10111'
    print(f"Binary: {x_dec:b}")
    print(f"Decimal: {x_dec:d}")    # default is 'd'
    print(f"Octal: {x_dec:o}")
    print(f"Hexadecimal: {x_dec:x}")

    x_dec = 0b0110
    print(f"Binary: {x_dec:b}")
    print(f"Decimal: {x_dec:}")
    print(f"Octal: {x_dec:o}")
    print(f"Hexadecimal: {x_dec:x}")

    x_dec = 0xFF
    print(f"Binary: {x_dec:b}")
    print(f"Decimal: {x_dec:}")
    print(f"Octal: {x_dec:o}")
    print(f"Hexadecimal: {x_dec:x}")

if __name__ == "__main__":
    # field_names()
    # format_width_and_padding()
    # format_with_precision()
    # format_percentage()
    # format_scientific_notation()
    format_bases()