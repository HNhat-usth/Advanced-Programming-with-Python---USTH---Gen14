def strListToStr(l: list):
    """
    turn a list of str into a str of the format:
    0. value1
    1. value2
    ...
    """
    new_str = ""
    for i, item in enumerate(l):
        new_str += f"{str(i)}. {str(item)} \n"
    return new_str


def inputNum(
    converter, message: str, input_name: str, lowerbound: int = 0, upperbound: int = 20
):
    """Repeatedly ask user to input a number in [lowerbound, upperbound]
    until it gets a valid number convertable by 'converter'"""
    user_input = ""
    while True:
        user_input = input(message)
        try:
            user_input = converter(user_input)
            if lowerbound > user_input or user_input > upperbound:
                print(
                    f"{input_name} is supposed to be > {lowerbound} and < {upperbound}"
                )
                continue
            break
        except ValueError:
            print(f"{input_name} is supposed to be a {converter.__name__}")
            continue
    return user_input


def pick(my_list, name):
    """Let user pick an index of a list and return it"""
    if my_list == []:
        print(f"There is no {name} registered")
    else:
        while True:
            index = inputNum(
                int,
                f"- Pick a {name} :\n" + strListToStr(my_list),
                "Index",
                0,
                len(my_list) - 1,
            )
            if 0 <= index and index < len(my_list):
                return index
            else:
                print("Invalid number")
    return -1
