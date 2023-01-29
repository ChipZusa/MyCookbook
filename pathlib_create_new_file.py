#! /usr/bin/env python3
"""Created by chris at 1/29/23

Example of creating a file with the Path.touch() method
Ref: https://realpython.com/lessons/creating-file/
"""
import pathlib

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

if __name__ == "__main__":
    create_new_file()

