from typing import List, Callable


def divide(num_1: int, num_2: int) -> float:
    return num_1 / num_2


# Should return int
def add(num_1: int, num_2: int) -> str:
    return num_1 + num_2


# You can even specify a function as a type by importing it from the typing module
def adder(func: Callable, text: str) -> None:
    print(func(text))

