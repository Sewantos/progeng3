import pytest

from tasks.data_structures.bracket_sequence.solution import (
    is_correct_bracket_seq,
)


@pytest.mark.parametrize(
    "seq, expected",
    [
        ("", True),
        ("()", True),
        ("[]", True),
        ("{}", True),
        ("(]", False),
        ("}]", False),
        ("([", False),
        ("{[()]}", True),
        ("({[]})", True),
        ("[{()()}]", True),
        ("(", False),
        ("{[()", False),
        ("[]]", False),
        ("(([]){})[]", True),
        ("(([]){}[]", False),
        ("(([]){})[]]", False),
    ],
)  # type: ignore[misc]
def test_bracket_seq(seq: str, expected: bool) -> None:
    assert is_correct_bracket_seq(seq) is expected
