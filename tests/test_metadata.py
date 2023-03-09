import h10awswrnglr as wr


def test_metadata():
    assert wr.__version__ == "2.20.0"
    assert wr.__title__ == "h10awswrnglr"
    assert wr.__description__ == "Pandas on AWS."
    assert wr.__license__ == "Apache License 2.0"
