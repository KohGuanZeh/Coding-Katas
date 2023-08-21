from typing import cast, TypedDict, Generic, TypeVar, Sequence, Optional

T = TypeVar("T")


class SlidingWindowConfigs(TypedDict):
    sliding_window_len: int
    look_ahead_len: int
    min_match: int


class LZ77Encoder:
    @staticmethod
    def encode(
        configs: SlidingWindowConfigs, input: str | list[int]
    ) -> list[tuple[int, int, Optional[str | int]]]:
        """
        Returns a list of triplets when a sequence is passed through an LZ77 Encoder.
        Format of the triplets would be (offset, length, item).\n
        Note that it is only possible for item to be None only if the triplet is the last in the sequence.
        This only occurs when the last item in the sequence is part of the longest match.
        """
        sliding_window = BufferedSlidingWindow(configs, input)
        encoding: list[tuple[int, int, Optional[str | int]]] = []
        while sliding_window._buffer_start != sliding_window._end:
            offset, length = sliding_window.get_longest_match()
            sliding_window.shift(length)
            char = cast(Optional[str | int], sliding_window.get_buffer_start_item())
            encoding.append((offset, length, char))
            sliding_window.shift(1)
        return encoding


class BufferedSlidingWindow(Generic[T]):
    def __init__(self, configs: SlidingWindowConfigs, seq_obj: Sequence[T]) -> None:
        self._seq_obj = seq_obj[:]
        self._configs = configs
        self._window_start = 0
        self._buffer_start = 0
        self._end = min(self._configs["look_ahead_len"], len(self._seq_obj))

    @property
    def window_start(self) -> int:
        """
        Returns the index of the sequence that signifies the start of the Sliding Window.
        """
        return self._window_start

    @property
    def buffer_start(self) -> int:
        """
        Returns the index of the sequence that signifies the start of the Look Ahead Buffer.\n
        Item in the sequence in which the index points to is not yet pushed to the Sliding Window.
        """
        return self._buffer_start

    @property
    def end(self) -> int:
        """
        Returns the index of the sequence that signifies the end of the Look Ahead Buffer.\n
        Maximum value of this property should be the length of the sequence.
        """
        return self._end

    @property
    def window_len(self) -> int:
        """
        Returns the total number of items in the Sliding Window.
        """
        return self._buffer_start - self._window_start

    def shift(self, shift_amt: int) -> None:
        """
        Shifts the Sliding Window by specified amount.
        """
        self._end = min(self._end + shift_amt, len(self._seq_obj))
        self._buffer_start = min(self._buffer_start + shift_amt, self._end)
        if self.window_len > self._configs["sliding_window_len"]:
            diff = self.window_len - self._configs["sliding_window_len"]
            self._window_start += diff

    def get_longest_match(self) -> tuple[int, int]:
        """
        Returns the offset and length of the longest match.\n
        Note that a match is only valid if the match length is more than or equal to min_match.\n
        Offset refers to the number of items left of the start of the Look Ahead Buffer
        that points to the first item of the match in the Sliding Window.\n
        Length refers to the total length of the match with reference to the Look Ahead Buffer.
        """
        if self._window_start == self._buffer_start:
            return 0, 0

        offset = 0
        length = 0
        min_match = max(1, self._configs["min_match"])
        for i in range(self._window_start, self._buffer_start):
            matched = 0
            for j in range(self._buffer_start, self._end):
                if self._seq_obj[i + matched] != self._seq_obj[j]:
                    break
                matched += 1
            if matched >= min_match and matched >= length:
                offset = self._buffer_start - i
                length = matched

        return offset, length

    def get_buffer_start_item(self) -> Optional[T]:
        """
        Returns the first item in the Look Ahead Buffer.
        """
        if self._buffer_start == len(self._seq_obj):
            return None
        return self._seq_obj[self._buffer_start]
