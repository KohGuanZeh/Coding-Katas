from exercises.exercise2.count_coins import (
    list_exchanges,
    append_to_coin_list,
    remove_from_denominations,
)

MOCK_DENOMINATIONS = set([1, 2, 3])


def test_should_have_no_exchanges_when_total_is_zero() -> None:
    assert len(list_exchanges(amount_left=0, denominations=MOCK_DENOMINATIONS)) == 0


def test_should_append_coin_to_list() -> None:
    assert 30 in append_to_coin_list(coin_list=[10, 20], coin=30)


def test_should_not_mutate_passed_coin_list_on_append() -> None:
    mock_list = [4, 5, 6]
    append_to_coin_list(coin_list=mock_list, coin=7)
    assert len(mock_list) == 3


def test_should_remove_coin_from_set() -> None:
    assert 11 not in remove_from_denominations(denominations=set([11, 12, 13]), coin=11)


def test_should_not_mutate_passed_denominations_on_remove() -> None:
    mock_set = set([60, 70, 80])
    remove_from_denominations(denominations=mock_set, coin=60)
    assert len(mock_set) == 3
