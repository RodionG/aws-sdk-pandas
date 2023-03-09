import logging

import pytest

import h10awswrnglr as wr

logging.getLogger("h10awswrnglr").setLevel(logging.DEBUG)


def test_chime_bad_input():
    with pytest.raises(ValueError):
        result = wr.chime.post_message(message=None, webhook=None)
        assert result is None
