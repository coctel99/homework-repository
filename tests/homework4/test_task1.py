import os

import pytest

from homework4.task1 import is_magic_number

TEST_FILE_PATH = "text.txt"


@pytest.fixture()
def file_content(request):
    """Get parameters from parametrize fixture and pass them to
    another fixture."""
    return request.param


@pytest.fixture(scope="function")
def create_temporary_file(file_content):
    with open(TEST_FILE_PATH, "w") as fi_correct:
        fi_correct.write(file_content)
        fi_correct.close()
    yield
    if os.path.exists(TEST_FILE_PATH):
        os.remove(TEST_FILE_PATH)


@pytest.mark.parametrize('file_content', ["1"], indirect=True)
def test_positive_case(create_temporary_file, file_content):
    """Testing that magic number in the first line of a file
    gives True."""
    if os.path.exists(TEST_FILE_PATH):
        assert is_magic_number(TEST_FILE_PATH)
    else:
        raise Exception("File not exist")


@pytest.mark.parametrize('file_content', ["123"], indirect=True)
def test_negative_case(create_temporary_file, file_content):
    """Testing that non-magic number in the first line of a file
    gives False."""
    if os.path.exists(TEST_FILE_PATH):
        assert not is_magic_number(TEST_FILE_PATH)
    else:
        raise Exception("File not exist")


@pytest.mark.parametrize('file_content', ["abvdef"], indirect=True)
def test_value_error_case(create_temporary_file, file_content):
    """Testing that not a number in the first line of a file raises
    ValueError."""
    if os.path.exists(TEST_FILE_PATH):
        assert ValueError
    else:
        raise Exception("File not exist")
