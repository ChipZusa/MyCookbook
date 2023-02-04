#! /usr/bin/env python3
"""Created by chris at 2/2/23

Using property() to access attributes
    step-by-step development with a final version Person
    a template "prop" class is included at the end
Ref: https://www.pythontutorial.net/python-oop/python-properties/
Using @property to access attribures
Ref: https://www.pythontutorial.net/python-oop/python-property-decorator/
"""

# pylint: disable=too-few-public-methods
class PersonTry1:
    """Demo class"""

    def __init__(self, name, age):
        self.name = name
        self.age = age


class PersonTry2:
    """Demo with getter and setter"""

    def __init__(self, name, age):
        self.name = name
        self.set_age(age)  # actual age gets set in a private variable

    def set_age(self, age: float) -> None:
        """setter for age attribute"""
        if age <= 0:
            raise ValueError("The age must be positive")
        self._age = age  # _age finally gets set ... not directly in init

    def get_age(self) -> float:
        """getter for age attribute"""
        return self._age


class PersonTry3:
    """Demo using property()"""

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def set_age(self, age):
        """fset function for property()"""
        if age <= 0:
            raise ValueError("The age must be positive")
        self._age = age
        # Note on above: I find it odd when instance variables are defined
        # within methods and not noted in the init()

    def get_age(self):
        """fget function for property()"""
        return self._age

    age = property(fget=get_age, fset=set_age)  # a new property object


class PersonTry4:
    """Using property to accept a callable and return a callable"""

    def __init__(self, name, age):
        self.name = name
        self._age = age  # this is comforting: now _age is defined in the init

    def age(self):
        return self._age

    age = property(fget=age)
    # print(help(age))
    # Note: this is similar to Try3 except the name of the
    # property is identical to the name of the method.
    # It recognizes the property name as a method to be run.


class PersonTry5:
    """Next step: use @property to replace the
    explicit use of the property() function.
    Can now added a setter and use the decorator technique"""

    def __init__(self, name, age):
        self.name = name
        self._age = age

    @property
    def age(self):
        return self._age

    # replace the method and setter with...
    def set_age(self, value):
        """a setter for the age property"""
        if value <= 0:
            raise ValueError("The age must be positive")
        self._age = value

    age = age.setter(set_age)


# class PersonTry6:
class PersonTry6:
    """The explicit property setter() method can also
    be replaced by a decorator. Since the property receives
    a callable and returns a callable of the same name,
    the setter method is renamed to 'age'"""

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    def age(self):
        return self._age

    @age.setter
    # def set_age(self, value):
    def age(self, value):  # this has been renamed
        """a setter for the age property"""
        if value <= 0:
            raise ValueError("The age must be positive")
        self._age = value

# Next: add the name property on your own
class Person:
    """Adding property/decorator for name"""

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    def name(self) -> str:
        """A getter to return a name"""
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        """A setter for the name attribute"""
        if not isinstance(name, str):
            raise ValueError("The name must be a string")
        self._name = name.capitalize()


    @property
    def age(self):
        return self._age

    @age.setter
    # def set_age(self, value):
    def age(self, value):  # this has been renamed
        """a setter for the age property"""
        if value <= 0:
            raise ValueError("The age must be positive")
        self._age = value

class MyClass:
    """Use decorators to create a property following
    this pattern."""
    def __init__(self, attr):
        self.prop = attr

    @property
    def prop(self):
        return self.__attr

    @prop.setter
    def prop(self, value):
        self.__attr = value

if __name__ == "__main__":

    jill = Person("Jill", 13)
    print(jill.name)
    print(jill.age)
    jill.name = "betty"
    jill.age = 10
    print(jill.name)
    print(jill.age)
    # jill.name = 10 # should be an error
    # jill.age = -1 # should be an error
