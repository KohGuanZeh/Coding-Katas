from exercises.exercise1.fizzbuzz import fizzbuzz, count_to


class CountTracker:
    def __init__(self) -> None:
        self.counted = 0

    def add_count(self) -> None:
        self.counted += 1


def test_should_count_up_to_number() -> None:
    count_tracker = CountTracker()
    count_to(9, lambda value: count_tracker.add_count())
    assert count_tracker.counted == 9


class Logger:
    def __init__(self) -> None:
        self.logs: list[str] = []

    def log_fizzbuzz(self, value: int) -> None:
        self.logs.append(fizzbuzz(value))


def test_render_fizzbuzz() -> None:
    logger = Logger()
    count_to(5, logger.log_fizzbuzz)
    assert logger.logs == ["1", "2", "Fizz", "4", "Buzz"]
