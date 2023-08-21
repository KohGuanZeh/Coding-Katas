def list_exchanges(
    amount_left: int, denominations: set[int], coin_list: list[int] = []
) -> list[list[int]]:
    """
    List all possible coin exchanges based on the amount given,
    possible set of denominations,
    and existing coins included in the exchange.
    """
    exchanges: list[list[int]] = []

    if amount_left == 0 and coin_list:
        exchanges.append(coin_list)
    elif amount_left > 0 and denominations:
        coin = next(iter(denominations))
        exchanges.extend(
            list_exchanges(
                amount_left - coin,
                denominations.copy(),
                append_to_coin_list(coin_list, coin),
            )
        )
        exchanges.extend(
            list_exchanges(
                amount_left,
                remove_from_denominations(denominations, coin),
                coin_list.copy(),
            )
        )

    return exchanges


def append_to_coin_list(coin_list: list[int], coin: int) -> list[int]:
    """
    Returns a copy of coin list with the specified coin appended.
    Note that the original list will not be modified.
    """
    coin_list_copy = coin_list.copy()
    coin_list_copy.append(coin)
    return coin_list_copy


def remove_from_denominations(denominations: set[int], coin: int) -> set[int]:
    """
    Returns a copy of the set of denominations with the specified coin removed.
    Note that the original set will not be modified.
    """
    denominations_copy = denominations.copy()
    denominations_copy.remove(coin)
    return denominations_copy


def run_coin_exchange() -> None:
    exchanges = list_exchanges(amount_left=15, denominations=set([1, 5, 10, 25]))
    print(f"\nThere are {len(exchanges)} ways to exchange: \n")
    for coin_list in exchanges:
        print(f"{coin_list}\n")


if __name__ == "__main__":
    run_coin_exchange()
