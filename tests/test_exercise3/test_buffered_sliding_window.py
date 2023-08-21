from exercises.exercise3.lz77_encoder import BufferedSlidingWindow, SlidingWindowConfigs

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


def test_shift_should_point_to_correct_indexes() -> None:
    mock_seq = [0, 1, 2, 3, 4]
    sliding_window = BufferedSlidingWindow(MOCK_CONFIGS, mock_seq)
    sliding_window.shift(4)
    assert sliding_window.window_start == 0
    assert sliding_window.buffer_start == 4
    assert sliding_window.end == 5


def test_get_longest_match_abra_after_shift_3_should_return_3_1() -> None:
    mock_seq = "abra"
    sliding_window = BufferedSlidingWindow(MOCK_CONFIGS, mock_seq)
    sliding_window.shift(3)
    assert sliding_window.get_longest_match() == (3, 1)


def test_get_longest_match_abra_with_min_match_more_than_1_after_shift_3_should_return_0_0() -> (
    None
):
    mock_seq = "abra"
    sliding_window = BufferedSlidingWindow(MOCK_MIN_MATCH_CONFIGS, mock_seq)
    sliding_window.shift(3)
    assert sliding_window.get_longest_match() == (0, 0)


def test_get_first_buffer_item_should_return_h() -> None:
    mock_seq = "hello"
    sliding_window = BufferedSlidingWindow(MOCK_CONFIGS, mock_seq)
    assert sliding_window.get_buffer_start_item() == "h"


def test_get_first_buffer_item_when_buffer_is_empty_return_none() -> None:
    mock_seq = "another test"
    sliding_window = BufferedSlidingWindow(MOCK_CONFIGS, mock_seq)
    sliding_window.shift(100)
    assert sliding_window.get_buffer_start_item() == None
