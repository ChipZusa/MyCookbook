#! /usr/bin/env python3
"""Demonstration of several methods to print binary strings
    - print_bit_sequence
    - print_bits_from_ascii_string
    - print_binary_unicode_string
"""
# pylint: disable=pointless-string-statement

# Print a byte-separated binary string of ascii characters
def print_bit_sequence(astring: str) -> str:
    """Print a byte-separated binary string of ascii characters."""
    if not astring.isascii():
        raise ValueError("ASCII only allowed")
    return " ".join(f"{ord(i):08b}" for i in astring)


# Print binary, ascii values, and character strings
def print_bits_from_ascii_string(
    the_string: str = "Plain string",
    num_switch: bool = False,
    char_switch: bool = False,
) -> str:
    """Print binary, ascii values, and character strings"""
    list_of_string = list(the_string)
    bit_list = ""
    for char in list_of_string:
        bit_list += format(ord(char), "08b")
        # if decimal switch set, add number to the end
        if num_switch:
            bit_list += " " + str(ord(char))
        # if char switch set, add char to the end
        if char_switch:
            bit_list += " " + char
        bit_list += "\n"
    return bit_list


# Print the binary unicode string of characters
def print_binary_unicode_string() -> str:
    """Print the binary unicode string of characters"""
    astring = "abc🃞de"
    result = ""
    for char in astring:
        result = result + f"{ord(char):08b}\n"
    return result


if __name__ == "__main__":

    # print(print_bits_from_ascii_string("Fred", num_switch=True, char_switch=True))  # okay
    # print("------------------------------------------------")
    # print(print_bits_from_ascii_string("🃞", num_switch=True, char_switch=True))  # okay
    # print("------------------------------------------------")
    # print(print_bit_sequence("Hello, World!"))  # okay
    # print("------------------------------------------------")
    print(print_binary_unicode_string())  # okay
