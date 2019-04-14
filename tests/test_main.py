from spaceman import Spaceman


def test_local_checkpoint():
    with Spaceman(bucket="checkpoint-location") as check:
        item = check.store(["one", {}])
        assert item is not None
        assert isinstance(item.loc, str)
    # raise Exception
