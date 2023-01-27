#! /usr/bin/env python3
"""Created by chris at 1/26/23

1. Creating Path Objects From Strings, methods home() and cwd(),
    and the method joinpath() and its short cut slash operator
2. Using exists(), is_file(), and is_dir()
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

def related_pathlib_functions():
    """Demo of exists(), is_file(), and is_dir()"""
    path_home = pathlib.Path.home()
    path_desktop = path_home / "Desktop"
    path_docs = path_home / "Documents"

    hi_desk = path_desktop / "hello.txt"
    hi_docs = path_docs / "hello.txt"

    print(repr(hi_desk))
    print(repr(hi_docs))

    print(f"hi_desk exists? {hi_desk.exists()}")
    print(f"hi_docs exists? {hi_docs.exists()}")
    print()
    print("Check if hello.txt is a file or directory")
    print(f"Is hello.txt a file? {hi_docs.is_file()}")
    print(f"Is hello.txt a directory? {hi_docs.is_dir()}")
    print(f"Is Documents a directory? {path_docs.is_dir()}")
    print(f"Is Documents a file? {path_docs.is_file()}")

    # One gotcha to remember
    # is_file and is_dir return False if the path does not exist
    print(f"Using exists() we get: {hi_desk.exists()}")
    print(f"Using is_file() we get: {hi_desk.is_file()}")
    print(f"Using is_dir() we get: {hi_desk.is_dir()}")

def check_if_path_exists(the_path):
    """Demo of methods exists(), is_file(), and is_dir()"""
    if the_path.exists():
        check_if_file_or_directory(the_path)
    else:
        print(f"The path '{the_path}' does not exist.")

def check_if_file_or_directory(the_path):
    """Demo of is_file() and is_dir"""
    # the_path = pathlib.Path("This/bogus/path")
    if the_path.exists() and the_path.is_file():
        print(f"'{the_path}' is a file")
    elif the_path.exists() and the_path.is_dir():
        print(f"'{the_path}' is a directory")
    else:
        if not the_path.exists():
            print(f"'{the_path}' does not exist")


if __name__ == "__main__":
    # create_path_object()
    some_path = pathlib.Path.cwd()
    check_if_file_or_directory(some_path)
    #
    some_path = some_path / "zippitydo"
    check_if_file_or_directory(some_path)
    #
    some_path = pathlib.Path.cwd() / __file__
    check_if_file_or_directory(some_path)
    # check_if_path_exists(some_path)
    #
    # related_pathlib_functions()