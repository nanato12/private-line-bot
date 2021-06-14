from abc import ABCMeta
from typing import Optional, Tuple

from core.utils import is_executable_command


class BaseCommand(metaclass=ABCMeta):
    cmd: str
    description: str

    @classmethod
    def is_executable_with_arg(cls, text: str) -> Tuple[bool, Optional[str]]:
        return is_executable_command(text, cls.cmd)

    @classmethod
    def is_executable(cls, text: str) -> bool:
        return cls.is_executable_with_arg(text) == (True, None)
