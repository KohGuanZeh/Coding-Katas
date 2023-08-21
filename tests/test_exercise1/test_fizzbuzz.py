from exercises.exercise1.fizzbuzz import fizzbuzz


def test_should_return_integer_for_non_multiples_of_three_and_five() -> None:
    assert fizzbuzz(1) == "1"


def test_should_return_fizz_for_multiples_of_three() -> None:
    assert fizzbuzz(3) == "Fizz"


def test_should_return_buzz_for_multiples_of_five() -> None:
    assert fizzbuzz(5) == "Buzz"


def test_should_return_fizzbuzz_for_multiples_of_three_and_five() -> None:
    assert fizzbuzz(15) == "FizzBuzz"
