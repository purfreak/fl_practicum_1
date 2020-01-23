from main import *


def iowrapper(function, arguments):
    import sys
    import io

    old_stdout = sys.stdout
    sys.stdout = buffer = io.StringIO()

    function(*arguments)

    sys.stdout = old_stdout
    return buffer.getvalue()


def test_main_yes():
    from test_data import DATA_YES_1, DATA_YES_2
    assert iowrapper(main, DATA_YES_1) == "YES\n"
    assert iowrapper(main, DATA_YES_2) == "YES\n"


def test_main_no():
    from test_data import DATA_NO_1
    assert iowrapper(main, DATA_NO_1) == "NO\n"


def test_main_re_exception_not_enough_elements_on_stack():
    assert iowrapper(main, ("ab+b*aa*", "a", "4")).startswith("Incorrect Regular expression:")


def test_main_re_exception_too_many_elements_on_stack():
    assert iowrapper(main, ("b+b*aa*", "a", "4")).startswith("Incorrect Regular expression:")


def test_main_re_exception_incorrect_symbol():
    assert iowrapper(main, ("abcd", "a", "2")).startswith("Incorrect Regular expression:")


def test_main_unknown_exception_wrong_argument():
    assert iowrapper(main, ("a", "a", "abc")).startswith("Unknown exception:")


def test_main_unknown_exception_zero_division_error():
    assert iowrapper(main, ("aba.*.a.*ab1+..", "a", "0")).startswith("Unknown exception:")
