"""
Write a function that will receive a string and write it to stderr
if line starts with "error" and to the stdout otherwise.
my_precious_logger("error: file not found")
# stderr
'error: file not found'
my_precious_logger("OK")
# stdout
'OK'
Definition of done:
 - function is created
 - function is properly formatted
 - function has positive tests
You will learn:
 - how to write to stderr
 - how to test output to the stderr and stdout
"""
import sys


def my_precious_logger(text: str):
    """
    Print text to stderr or stdout

    Text is printed to stderr if it starts with 'error'. Otherwise,
    text is printed to stdout

    Function duplicates the output to corresponding .txt files
    :param text: Text to print
    """
    if text.startswith("error"):
        sys.stderr = open("stderr.txt", "w")
        print(text, file=sys.stderr)
        sys.stderr.close()
    else:
        sys.stdout = open("stdout.txt", "w")
        print(text)
        sys.stdout.close()
