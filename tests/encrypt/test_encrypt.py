import pytest
from challenges.challenge_encrypt_message import encrypt_message


def test_encrypt_message():

    # Valid types
    assert encrypt_message("jazzbo", 100) == "obzzaj"

    assert encrypt_message("jazzbo", 3) == "zaj_obz"

    assert encrypt_message("jazzbo", 4) == "ob_zzaj"

    # Invalid types
    with pytest.raises(TypeError):
        encrypt_message(13, 4)

    with pytest.raises(TypeError):
        encrypt_message("fake", "f")
