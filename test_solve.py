from solve import *


def test_solver_is_funcs():
    ops_binary = {".", "+"}
    ops_repeat = {"*"}
    alphabet = {"a", "b", "c"}
    empty_words = {"1"}

    all_valid_symbols = ops_binary | ops_repeat | alphabet | empty_words

    all_symbols = all_valid_symbols | {"2", "3", ",", " ", "d", "e"}

    not_ops_binary = all_symbols - ops_binary
    not_ops_repeat = all_symbols - ops_repeat
    not_alphabet = all_symbols - alphabet
    not_empty_words = all_symbols - empty_words

    for op in ops_binary:
        assert Solver.is_binary_operator(op)

    for op in ops_repeat:
        assert Solver.is_repeat_operator(op)

    for a in alphabet:
        assert Solver.is_letter(a)

    for e in empty_words:
        assert Solver.is_empty_word(e)

    for not_op in not_ops_binary:
        assert not Solver.is_binary_operator(not_op)

    for not_op in not_ops_repeat:
        assert not Solver.is_repeat_operator(not_op)

    for not_a in not_alphabet:
        assert not Solver.is_letter(not_a)

    for not_e in not_empty_words:
        assert not Solver.is_empty_word(not_e)


def test_solver_solve_true():
    from test_data import DATA_YES_1, DATA_YES_2
    assert Solver(*DATA_YES_1).solve()
    assert Solver(*DATA_YES_2).solve()


def test_solver_solve_false():
    from test_data import DATA_NO_1
    assert not Solver(*DATA_NO_1).solve()
