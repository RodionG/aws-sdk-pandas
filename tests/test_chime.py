import logging

import pytest

import h10_awswrangler as wr

logging.getLogger("h10_awswrangler").setLevel(logging.DEBUG)


def test_chime_bad_input():
    with pytest.raises(ValueError):
        result = wr.chime.post_message(message=None, webhook=None)
        assert result is None
