#! /usr/bin/env python3
"""Created by chris at 2/6/23

Dictionaries, lists, sets, and tuple classes. And maybe
something from the collections module
Ref: https://docs.python.org/3/library/stdtypes.html#mapping-types-dict
"""
from pprint import pprint

class DictOps:
    """Examples of creating and loading dicts"""

    def __init__(self):
        # Creating dicts
        # 1. comma-separated list of Key: value pairs
        self.new_dict = {}
        self.dict_1 = {"jack": 25, "jill": 22, "red hen": 1.5}

        # 2. using the dict() constructor
        self.new_dict = dict()  # {} is faster, avoids extra fun call
        self.dict_2 = dict([("one", 100), ("two", 200), ("three", 300)])
        self.dict_3 = dict(foo=300, bar=900, foobar=7)
        # print(self.dict_2)
        # zip to lists and make a dict.

    def make_dict(self):
        """Examples of various ways of creating a dict"""
        # from two strings
        word = "hello"
        index = "01234"
        # zip_iterator = zip(index, word)
        # list_zip = list(zip_iterator)
        # dict_zip = dict(list_zip)

        dict_zip = dict(zip(index, word))

        print(f"dict_zip is type: {type(dict_zip)}")
        # print(f"and looks like this: \n  {dict_zip}")
        # print(f"dict_zip['1'] is {dict_zip['1']}")

        # from two lists
        list1 = [0, 1, 2, 3, 4]
        list2 = list("hello")

        dict_list = dict(zip(list1, list2))

        print(f"dict_list: {dict_list}")
        # print("A:",dict_list )

        # from enumeration
        dict_enum = dict(enumerate(list2))

        print(f"dict_enum is {dict_enum}")

        # from comprehension
        dict_comp = {x: x**2 for x in range(5)}
        print(f"dict_comp is {dict_comp}")

    def operations_with_dicts(self):
        """Some operations, what they return
        and what types"""
        # Return a list of all the keys used in the dictionary d.
        key_list = list(self.dict_3)
        print(f"key_list is: {key_list} \nand is of type {type(key_list)}")

        # Return the integer number of items in a dict
        num_items_in_dict = len(key_list)
        print(f"number of items in dict: {num_items_in_dict}")
        print(f"and is of {type(num_items_in_dict)}")

        # Return the item using the key
        item_value = self.dict_3["bar"]
        print(f"value for 'bar' is: {self.dict_3['bar']}")
        print(f"and is the type stored in the value. Here, {type(item_value)}")
        try:
            bogus_value = self.dict_3["fee"]
        except KeyError as error:
            print(error)
            print(f"KeyError: {error} is not in the map")

        # set value of an item
        self.dict_3["new"] = 32
        print(f"dict is now: {self.dict_3}")

        # Check if a key is in a dict
        is_here = "new" in self.dict_3
        print(f"is_here is {is_here}")

        # Return an iterator over the keys of the dictionary.
        key_iterator = iter(self.dict_3)
        for _ in key_iterator:
            print(_)

        # Return a shallow copy of the dict
        dict_copy = self.dict_3.copy()
        print(f"dict_copy == self.dict_3: {dict_copy == self.dict_3}")

        # Remove a key and return its value
        dict_item = dict_copy.pop("foo")
        print(f"value popped is {dict_item}")
        print(f"dict_copy is now:\n    {dict_copy}")

        # Remove and return a tuple (key, value) pair...in LIFO order.
        # Useful for destructively iterating over a dictionary.
        num = len(dict_copy)
        try:
            for _ in range(num):
                item = dict_copy.popitem()
                print(item)
        except KeyError as error:
            print(error)

        # Update the dictionary with the key/value pairs from other,
        # overwriting existing keys. Return None.
        other = dict(dave='brother', mary='sister', ruth='mother')
        self.dict_3.update(other)
        pprint(f"self.dict_3 is now: {self.dict_3}")



if __name__ == "__main__":

    mydict = DictOps()
    # Three ways to create dicts and the result
    # print(mydict.dict_1)
    # print(mydict.dict_2)
    # print(mydict.dict_3)

    # mydict.make_dict()

    mydict.operations_with_dicts()
