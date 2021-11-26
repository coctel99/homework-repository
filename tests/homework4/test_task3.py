import os

import pytest

from homework4.task3 import my_precious_logger

ERROR_STRING = "error: file not found"
OK_STRING = "OK"


@pytest.fixture(scope="function")
def clean_up():
    """Remove stderr.txt and stdout.txt before every test function."""
    if os.path.exists("stderr.txt"):
        os.remove("stderr.txt")
    if os.path.exists("stdout.txt"):
        os.remove("stdout.txt")


def test_output_to_stderr_only(clean_up):
    """Testing that error message prints only to stderr."""
    my_precious_logger(ERROR_STRING)
    assert open("stderr.txt").read().strip() == ERROR_STRING and not \
        os.path.exists("stdout.txt")


def test_output_to_stdout_only(clean_up):
    """Testing that non-error message prints only to stdout."""
    my_precious_logger(OK_STRING)
    assert open("stdout.txt").read().strip() == OK_STRING and not \
        os.path.exists("stderr.txt")


def test_output_to_stderr_and_stdout(clean_up):
    """Testing that error and non-error messages are printed both to
    stderr and to stdout."""
    my_precious_logger(ERROR_STRING)
    my_precious_logger(OK_STRING)
    assert open("stderr.txt").read().strip() == ERROR_STRING and \
        open("stdout.txt").read().strip() == OK_STRING
