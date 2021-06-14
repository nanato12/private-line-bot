import re
from typing import Optional, Tuple


def convert_camel_case(s: str) -> str:
    """convert to camel case

    Args:
        s (str): str

    Returns:
        str: camel case str
    """
    return s.title().replace("_", "").replace("-", "")


def extract_alphabet(s: str) -> str:
    """extract only alphabet

    Args:
        s (str): str

    Returns:
        str: only alphabet str
    """
    return re.sub(r"[^a-zA-Z]", "", s)


def is_executable_command(s: str, cmd: str) -> Tuple[bool, Optional[str]]:
    """determine executable command

    Args:
        s (str): str
        cmd (str): command

    Returns:
        Tuple[bool, Optional[str]]: judge, argument
    """
    length: int = len(cmd)
    is_executable: bool = s[:length] == cmd
    return (
        is_executable,
        s[length:] if is_executable and s[length:] != "" else None,
    )
