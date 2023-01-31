#! /usr/bin/env python3
"""Created by chris at 1/26/23

1. Creating Path Objects From Strings, methods home() and cwd(),
    and the method joinpath() and its short cut slash operator
2. Using exists(), is_file(), and is_dir()
"""
import pathlib
from pathlib import Path

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


def create_new_file():
    """Demo of creating a new file using the instance
        method Path.touch()"""
    """Steps
    1. Create a path for a directory
    2. Ensure it is not already a directory (for learning)
    3. Create the directory (using flag parents=True)
    4. Create a file inside this new directory
    """
    #     1. Create a path for a directory
    new_path_string = pathlib.Path.home()
    new_dir_path = new_path_string / "practice" / "monthly_dir"
    # print(new_dir_path)
    #     2. Ensure it is not already a directory (for learning)
    # print(new_dir_path.exists())
    #     3. Create the directory
    #       (using flag parents=True,
    #       and exist_ok=True so I can rerun without errors)
    new_dir_path.mkdir(exist_ok=True, parents=True)
    # print(new_dir_path.is_dir())
    #     4. Create a file inside this new directory
    # So, create a january_path file inside of the monthly_dir, and I’ll call it "january.txt".
    january_path = new_dir_path.joinpath("january.txt")
    # print(january_path)

    january_path.touch()    # file is finally created

    print(f"'{january_path} exists: {january_path.exists()}")
    print(f"...and '{january_path}' is a file: {january_path.is_file()}")

def is_file_is_dir_and_exists():
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


def iterate_over_directory():
    # Create a path to a directory and ensure it exists
    current_dir = pathlib.Path.cwd()
    if not current_dir.exists():
        print(f"Warning! Directory '{current_dir}' does not exist")

    # Create a generator for iterating over the directory
    current_iterable = current_dir.iterdir()
    print(f"Type of current_iterable is: {type(current_iterable)}")

    # and lets see them
    for item in current_iterable:
        print(item)
    # or ... "for item in current_dir.iterdir()" in one step



def rename_move():
    """https://learnpython.com/blog/how-to-rename-files-python/"""
    # define file path that we want to rename
    filepath = Path.cwd() / "photos" / "shooting_star.png"
    # rename file
    filepath.rename(Path.cwd() / "photos" / "shooting_star2.png")

    # define directory path that we want to rename
    dir_path = Path.cwd() / "photos"
    # change directory name
    dir_path.rename(Path.cwd() / "pics")
    print(filepath)
    print(dir_path)

def glob_over_directory():
    """Given a relative pattern, yield all matching files"""
    # Obtain a path to the directory to be searched
    current_dir = pathlib.Path.cwd()

    # Search for all "py" files
    pattern = "*.py"
    pattern1 = "[b][i][t][es].py"
    pattern2 = "*.[p][y]"
    pattern3 = "*.[pt][xy]*"
    glob_generator = current_dir.glob(pattern3)
    for _ in glob_generator:
        print(_)

    # Recursive into all lower directories
    glob_generator = current_dir.glob("**/*.py")
    # or
    glob_generator = current_dir.rglob("*.py")

def pathlib_shutil_copy_file():
    """Combine use of pathlib and shutil to copy a file"""
    from shutil import copyfile

    source = Path('words.txt')
    destination = Path('words_bck.txt')

    copyfile(source, destination)



if __name__ == "__main__":
    # create_path_object()
    # some_path = pathlib.Path.cwd()
    # check_if_file_or_directory(some_path)
    #
    # some_path = some_path / "zippitydo"
    # check_if_file_or_directory(some_path)
    #
    some_path = pathlib.Path.cwd() / __file__
    check_if_file_or_directory(some_path)
    # check_if_path_exists(some_path)
    #
    # is_file_is_dir_and_exists()
    # create_new_file()
    # iterate_over_directory()
    rename_move()