import logging
import os

import pytest

from h10awswrnglr._utils import ensure_cpu_count, get_even_chunks_sizes

logging.getLogger("h10awswrnglr").setLevel(logging.DEBUG)


@pytest.mark.parametrize(
    "total_size,chunk_size,upper_bound,result",
    [
        (10, 4, True, (4, 3, 3)),
        (2, 3, True, (2,)),
        (1, 1, True, (1,)),
        (2, 1, True, (1, 1)),
        (11, 4, True, (4, 4, 3)),
        (1_001, 500, True, (334, 334, 333)),
        (1_002, 500, True, (334, 334, 334)),
        (10, 4, False, (5, 5)),
        (1, 1, False, (1,)),
        (2, 1, False, (1, 1)),
        (11, 4, False, (6, 5)),
        (1_001, 500, False, (501, 500)),
        (1_002, 500, False, (501, 501)),
    ],
)
def test_get_even_chunks_sizes(total_size, chunk_size, upper_bound, result):
    assert get_even_chunks_sizes(total_size, chunk_size, upper_bound) == result


@pytest.mark.parametrize("use_threads,result", [(True, os.cpu_count()), (False, 1), (-1, 1), (1, 1), (5, 5)])
def test_ensure_cpu_count(use_threads, result):
    assert ensure_cpu_count(use_threads=use_threads) == result
