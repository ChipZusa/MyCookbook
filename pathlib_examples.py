#! /usr/bin/env python3
"""Created by chris at 1/26/23

Creating Path Objects From Strings, methods home() and cwd(),
and the method joinpath() and its short cut slash operator
"""
import pathlib


def create_path_object():
    """Three ways to create objects that represent file paths"""
    # file path from a string
    print("File path from a string")
    the_path = pathlib.Path("/home/chris/Documents/Python/file_system_operations/pathlib_examples.py")
    print(repr(the_path))  # repr() shows a canonical version of the path
    print(the_path)
    print()

    # file path using class methods home() and cwd()
    print("File path from methods home() and cwd()")
    the_path = pathlib.Path.home()
    print(f"My home directory is '{the_path}'")
    the_path = pathlib.Path.cwd()
    print(f"My current working directory is '{the_path}'")
    print()

    # file using the forward slash operator
    print("File path using the forward slash operator")
    my_home_path = pathlib.Path.home()
    my_home_path = my_home_path / "Documents" / "test.txt"
    print(f"The new file path is '{the_path}'")
    # or
    new_path = pathlib.Path("test.txt")
    new_path = "/chris" / new_path  # Warning only one str ahead of the object
    # two strings or more is an error. Leading strings must be
    # anchored to the object
    # This is wrong: "/chris" / "Documents" / new_path
    print(f"The new file path is '{new_path}'")
    print()

    # file using .joinpath() method
    print("File path using the joinpath() method")
    joined_path = pathlib.Path("/home").joinpath("chris", "Documents", "test.txt")
    print(f"The joined path is '{joined_path}'")
    # or
    a_path = pathlib.Path.home()
    joined_path = a_path.joinpath("Documents", "test.txt")
    print(f"The joined path is '{joined_path}'")



if __name__ == "__main__":
    create_path_object()
