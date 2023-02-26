#! /usr/bin/env python3
"""Created by chris at 2/26/23


Ref: https://www.askpython.com/python/string/python-encode-and-decode-functions
"""

def encode_to_byes(a_string="This is a test."):
    """example of encoding a string into bytes"""
    to_bytes = a_string.encode()
    print(f"the byte string: {to_bytes}")
    return to_bytes

def decode_to_string(the_bytes=b'These were cute bytes.'):
    """example of decoding bytes into unicode"""
    to_string = the_bytes.decode()
    print(f"the string: {to_string}")
    return to_string


if __name__ == "__main__":
    in_bytes = encode_to_byes()
    # print(in_bytes)
    decode_to_string()

