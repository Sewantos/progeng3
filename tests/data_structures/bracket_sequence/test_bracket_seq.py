from tasks.data_structures.bracket_sequence.solution import (
    is_correct_bracket_seq,
)


def test_empty_strings():
    assert is_correct_bracket_seq("") is True


def test_simple_correct():
    assert is_correct_bracket_seq("()") is True
    assert is_correct_bracket_seq("[]") is True
    assert is_correct_bracket_seq("{}") is True


def test_simple_wrong():
    assert is_correct_bracket_seq("(]") is False
    assert is_correct_bracket_seq("}]") is False
    assert is_correct_bracket_seq("([") is False


def test_nested_correct():
    assert is_correct_bracket_seq("{[()]}") is True
    assert is_correct_bracket_seq("({[]})") is True
    assert is_correct_bracket_seq("[{()()}]") is True


def test_unclosed():
    assert is_correct_bracket_seq("(") is False
    assert is_correct_bracket_seq("{[()") is False
    assert is_correct_bracket_seq("[]]") is False


def test_complex_correct():
    assert is_correct_bracket_seq("(([]){})[]") is True


def test_complex_wrong():
    assert is_correct_bracket_seq("(([]){}[]") is False
    assert is_correct_bracket_seq("(([]){})[]]") is False
