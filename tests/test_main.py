from spaceman import Spaceman


def test_local_checkpoint():
    with Spaceman(bucket="checkpoint-location") as check:
        check.store(["one", {}])
    # raise Exception
