from spaceman.store import SpaceStorage

def test_add_local_storage():
    local_folder = "/tmp"
    storage = SpaceStorage(provider="local", local_folder=local_folder, folder_bucket_name="poop-dick")
    storage.add('klajsajsiaols', "helloworld.txt")
    # assert True == True
    # storage.add()

def test_add_s3_storage():
    """ We're testing to add S3 Storage"""
    local_folder = "/tmp"
    storage = SpaceStorage(
        provider="s3", local_folder=local_folder, folder_bucket_name="poop-dicks")
    storage.add('klajsajsiaols', "helloworld.txt")


def test_get_s3_storage():
    """ We're testing to add S3 Storage"""
    local_folder = "/tmp"
    storage = SpaceStorage(
        provider="s3", local_folder=local_folder, folder_bucket_name="poop-dicks")
    file_meta = storage.get("helloworld.txt")


    assert file_meta is not None
    assert file_meta['file'] is not None
    assert file_meta['exist'] == True
    assert file_meta['provider'] == "s3"
    assert file_meta['file'] == "klajsajsiaols"
    # print(file_meta["file"])
    # assert False
    # storage.add('klajsajsiaols', "helloworld.txt")

