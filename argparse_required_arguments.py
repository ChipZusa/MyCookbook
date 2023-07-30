#! /usr/bin/env python3
"""Created by chris at 7/22/23


Ref: https://docs.python.org/3/howto/argparse.html
"""
# raise NotImplementedError
# NOTpylint: disable=invalid-name use-dict-litera
import argparse


class ShowName:
    """Prints first and last name"""

    def __init__(self, first, last):
        self.first = first
        self.last = last

    def show_print(self):
        """prints first and last name to console"""
        print(f"{self.first} {self.last}")

    def show_verbose_print(self):
        """Prints a nicer message with the names"""
        print(f"Your first name is {self.first} and your last is {self.last}")

    def show_short_print(self):
        """A quick first and last name"""
        print(f"First name: '{self.first}'    Last name: '{self.last}'")


### argparse examples below ############################################
def positional_arguments():
    """argparse"""
    # here go the argparse stuff
    parser = argparse.ArgumentParser(description="Prints first and last name")
    parser.add_argument("first", help="First name must be the first argument")
    parser.add_argument("last", help="Last name must be the second argument")

    args = parser.parse_args()
    show = ShowName(args.first, args.last)
    show.show_print()


def optional_arguments_toggle():
    """introduced with -s or --something"""
    # use same first and last name arguments
    parser = argparse.ArgumentParser(description="Prints first and last name")
    parser.add_argument("first", help="First name must be the first argument")
    parser.add_argument("last", help="Last name must be the second argument")

    # now add the optional arguments
    # Note that action will store true and allow -v to be used as a toggle
    parser.add_argument(
        "-v",
        "--verbose",
        help="adds more text to the display",
        action="store_true",
    )

    args = parser.parse_args()
    show = ShowName(args.first, args.last)
    if args.verbose:
        show.show_verbose_print()
    else:
        show.show_print()


def optional_arguments_with_args():
    """choose an option to an argument with another argument"""
    # use same first and last name arguments
    parser = argparse.ArgumentParser(description="Prints first and last name")
    parser.add_argument("first", help="First name must be the first argument")
    parser.add_argument("last", help="Last name must be the second argument")

    # now add the optional arguments
    # This time the vebosity will expect an argument
    parser.add_argument(
        "-v",
        "--verbose",
        type=int,
        choices=[0, 1, 2],
        help="increase verbosity (1 or 2)",
    )

    args = parser.parse_args()
    show = ShowName(args.first, args.last)
    if args.verbose == 2:
        show.show_verbose_print()
    elif args.verbose == 1:
        show.show_short_print()
    else:
        show.show_print()


def optional_arguments_count():
    """using multiple args like -vv"""
    parser = argparse.ArgumentParser(description="Prints first and last name")
    parser.add_argument("first", help="First name must be the first argument")
    parser.add_argument("last", help="Last name must be the second argument")

    # now add the optional arguments
    # This time the vebosity will expect an argument
    parser.add_argument(
        "-v",
        "--verbosity",
        action="count",
        default=0,
        help="increase output verbosity",
    )

    args = parser.parse_args()
    show = ShowName(args.first, args.last)
    if args.verbosity >= 2:
        show.show_verbose_print()
    elif args.verbosity == 1:
        show.show_short_print()
    else:
        show.show_print()


def optional_arguments_without_clashing():
    """keep conflicting options from being run - requires a group"""
    parser = argparse.ArgumentParser(description="Prints first and last name")

    # now add the optional arguments

    parser.add_argument("first", help="First name must be the first argument")
    parser.add_argument("last", help="Last name must be the second argument")

    # Requires a group to prevent clashing
    group = parser.add_mutually_exclusive_group()
    group.add_argument(
        "-v",
        "--verbosity",
        action="count",
        default=0,
        help="increase output verbosity",
    )
    group.add_argument(
        "-q", "--quiet", action="store_true", help="print short message"
    )

    args = parser.parse_args()
    show = ShowName(args.first, args.last)

    if args.quiet:
        show.show_print()
    elif args.verbosity >= 2:
        show.show_verbose_print()
    elif args.verbosity == 1:
        show.show_short_print()
    else:
        show.show_print()


if __name__ == "__main__":
    # positional_arguments()
    # optional_arguments_toggle()
    # optional_arguments_with_args()
    # optional_arguments_count()
    optional_arguments_without_clashing()
