from exercises.exercise3.lz77_encoder import SlidingWindowConfigs, LZ77Encoder

MOCK_CONFIGS: SlidingWindowConfigs = {
    "sliding_window_len": 32,
    "look_ahead_len": 8,
    "min_match": 0,
}

MOCK_MIN_MATCH_CONFIGS: SlidingWindowConfigs = {
    "sliding_window_len": 32,
    "look_ahead_len": 8,
    "min_match": 3,
}


def test_encode_to_triplets_a_should_return_0_0_a() -> None:
    assert LZ77Encoder.encode(MOCK_CONFIGS, "a") == [(0, 0, "a")]


def test_encode_to_triplets_abra_should_return_correct_tuples() -> None:
    assert LZ77Encoder.encode(MOCK_CONFIGS, "abra") == [
        (0, 0, "a"),
        (0, 0, "b"),
        (0, 0, "r"),
        (3, 1, None),
    ]


def test_encode_to_triplets_abracadabra_with_min_match_3_should_return_correct_tuples() -> (
    None
):
    assert LZ77Encoder.encode(MOCK_MIN_MATCH_CONFIGS, "abracadabra") == [
        (0, 0, "a"),
        (0, 0, "b"),
        (0, 0, "r"),
        (0, 0, "a"),
        (0, 0, "c"),
        (0, 0, "a"),
        (0, 0, "d"),
        (7, 4, None),
    ]
