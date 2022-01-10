from homework4.task3 import my_precious_logger

ERROR_STRING = "error: file not found"
OK_STRING = "OK"


def test_output_to_stderr_only(capsys):
    """Testing that error message prints only to stderr."""
    my_precious_logger(ERROR_STRING)
    captured = capsys.readouterr()
    assert captured.err.strip() == ERROR_STRING and \
           captured.out.strip() == ""


def test_output_to_stdout_only(capsys):
    """Testing that non-error message prints only to stdout."""
    my_precious_logger(OK_STRING)
    captured = capsys.readouterr()
    assert captured.err.strip() == "" and \
           captured.out.strip() == OK_STRING


def test_output_to_stderr_and_stdout(capsys):
    """Testing that error and non-error messages are printed both to
    stderr and to stdout."""
    my_precious_logger(ERROR_STRING)
    my_precious_logger(OK_STRING)
    captured = capsys.readouterr()
    assert captured.err.strip() == ERROR_STRING and \
           captured.out.strip() == OK_STRING
