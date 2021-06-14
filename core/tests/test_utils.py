from typing import Tuple

import pytest

from core.utils import (
    convert_camel_case,
    extract_alphabet,
    is_executable_command,
)


@pytest.mark.parametrize(
    "text, expected",
    [
        ("aiueo", "Aiueo"),
        ("camel_case", "CamelCase"),
        ("CAMEL_CASE", "CamelCase"),
        ("camel-case", "CamelCase"),
        ("CAMEL-CASE", "CamelCase"),
        ("cAMeL-CasE", "CamelCase"),
    ],
)
def test_convert_camel_case(text: str, expected: str) -> None:
    assert convert_camel_case(text) == expected


@pytest.mark.parametrize(
    "text, expected",
    [
        ("aiueo", "aiueo"),
        ("/help", "help"),
        ("1234qwerty", "qwerty"),
        ("[@;]_/.,mloew", "mloew"),
    ],
)
def test_extract_alphabet(text: str, expected: str) -> None:
    assert extract_alphabet(text) == expected


@pytest.mark.parametrize(
    "text, cmd, expected",
    [
        ("/mid", "/mid", (True, None)),
        ("aiueo", "/mid", (False, None)),
        ("/search:test_uid", "/search:", (True, "test_uid")),
        ("/search:", "/search:", (True, None)),
    ],
)
def test_is_executable_command(text: str, cmd: str, expected: Tuple[bool, str]) -> None:
    assert is_executable_command(text, cmd) == expected
