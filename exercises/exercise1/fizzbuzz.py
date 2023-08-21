from typing import Callable


def fizzbuzz(value: int) -> str:
    """
    Returns "Fizz" if multiple of 3.
    Returns "Buzz" if multiple of 5.
    Returns "FizzBuzz" if multiple of 3 and 5.
    Returns the number if does not match the above.
    """
    result = ""
    if value % 3 == 0:
        result += "Fizz"
    if value % 5 == 0:
        result += "Buzz"
    return str(value) if result == "" else result


def count_to(end: int, callback: Callable[[int], None] = lambda value: None) -> None:
    """
    Counts from 1 to given number (inclusive), executing the callback on each number.
    """
    for step in range(1, end + 1):
        callback(step)


def run_fizzbuzz() -> None:
    count_to(100, lambda value: print(fizzbuzz(value)))


if __name__ == "__main__":
    run_fizzbuzz()
