from typing import List

from core.generator import GeneratorUtil


class Management:
    argv: List[str]

    def __init__(self, argv: List[str]) -> None:
        self.argv = argv

    def execute(self) -> None:
        first_arg = self.argv[0]
        if first_arg.count(":") == 1:

            option, cmd = first_arg.split(":")
            if option == "gen":
                gen = GeneratorUtil(cmd, self.argv[1:])
                gen.execute()


def exec_from_command_line(argv: List[str]) -> None:
    """execute command from command-line

    Args:
        argv (List[str]): arguments

    Raises:
        Exception: not enough arguments
    """

    if len(argv) == 1:
        raise Exception("Not enough arguments.")
    else:
        m = Management(argv[1:])
        m.execute()
