#!/bin/python3
from int_to_binary import int_to_binary


def solution(n):
    if n > 2 ** 32 / 2 or n < 1:
        return -1

    binary_n = int_to_binary(n)

    maximum_gap_length = 0
    gap_length = 0

    xor = 0
    for digit in binary_n:
        xor ^= digit

        if xor == 1 and digit == 0:
            gap_length += 1

        if xor == 0 and digit == 1:
            if gap_length > maximum_gap_length:
                maximum_gap_length = gap_length

            gap_length = 0
            xor = 1

    return maximum_gap_length


if __name__ == '__main__':
    print(int_to_binary(328))

    assert solution(328) == 2
