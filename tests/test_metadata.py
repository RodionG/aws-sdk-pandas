import h10_awswrangler as wr


def test_metadata():
    assert wr.__version__ == "2.20.0"
    assert wr.__title__ == "h10_awswrangler"
    assert wr.__description__ == "Pandas on AWS."
    assert wr.__license__ == "Apache License 2.0"
