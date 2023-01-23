#! /usr/bin/env python3
"""Created by chris at 1/20/23
    Examples included:
    - UNIX time
    - current datetime
    - parsing strings with datetime
    - creating strings with datetime
    - timedelta calculations

Ref: https://www.youtube.com/watch?v=1uTAfHqAi0U&list=PLEtC2iwVrNRZdd5HqafuFMWjG-V_i16rO&index=34
"""

import time
import datetime

# pylint: disable=pointless-string-statement
"""Two main ways of dealing with time in Python
1. UNIX Timestamp (just a float)
2. Python datetime object (with lots of methods and instance attribues)
"""


def unix_time_example() -> None:
    """Request UNIX time"""
    current_time = time.time()
    print(f"current time from UNIX time: {current_time}")


def datetime_example() -> None:
    """Request a python datetime object holding the time"""
    current_time = datetime.datetime.today()
    print(f"current time from datetime.datetime.today(): {current_time}")


def datetime_parsing_example() -> None:
    """Parse a date and time from a string"""
    datetime_object = datetime.datetime.strptime(
        "2020-06-18 12:30:00", "%Y-%m-%d %H:%M:%S"
    )
    print(f"datetime object: {datetime_object}")


def datetime_formating_example() -> None:
    """Format a string representing the date and time"""
    # First, need an instance object to work from
    datetime_object = datetime.datetime.strptime(
        "2020-06-18 12:30:00", "%Y-%m-%d %H:%M:%S"
    )
    datetime_string = datetime_object.strftime("%Y-%m-%d %H:%M:%S")
    print(f"datetime string from parsing: {datetime_string}")
    default_string = datetime_object.ctime()
    print(f'the "common" default string from ctime(): {default_string}')


def datetime_duration_examples() -> None:
    """Calculate differences in time using datetime objects"""
    three_days_ago = datetime.datetime.now() - datetime.timedelta(days=3)
    print(f"Three days ago was {three_days_ago}\n or {three_days_ago.ctime()}")
    # Difference between two times is a timedelta object
    start_time = datetime.datetime.now()
    for x in range(1000):
        pass
    end_time = datetime.datetime.now()
    duration = end_time - start_time
    print(f"A duration is of type {type(duration)}\n with a value of {duration}")


if __name__ == "__main__":
    unix_time_example()
    datetime_example()
    datetime_parsing_example()
    datetime_formating_example()
    datetime_duration_examples()
