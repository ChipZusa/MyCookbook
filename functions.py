"""Demonstration of functions and some simple variations in using arguments.
    1. order to fit the order of the parameters
    2. default arguments
    3. arguments out of order requiring keywords
    """


def greet_user():
    """Generic greeting for users"""
    print("Hello!")
    print("Welcome")


def greet_user_by_name(name="user", greeting="Hello"):
    """Customized greeting"""
    print(greeting + ", " + name)

def cube(base_number):
    """Demo of function returning a value"""
    cubed_value = base_number * base_number * base_number
    return cubed_value


if __name__ == "__main__":

    greet_user()

    # name = input("What is your name? ")
    greet_user_by_name(
        input("What is your name? "), "Welcome"
    )  # uses specified arguments (given in order!)
    greet_user_by_name(input("What is your name? "))  # uses default greeting
    greet_user_by_name()  # Uses both defaults
    greet_user_by_name(
        greeting="Welcome", name="Nancy Drew"
    )  # arguments out of order, then must be explicit and specifiy which argument is which

    eleven_cubed = cube(11)
    print(eleven_cubed)
