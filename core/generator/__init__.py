from typing import List

from core.generator.commands.command_generator import CommandGenerator
from core.generator.enviroments.env_generator import EnvGenerator
from core.generator.events.event_generator import EventGenerator


class GeneratorUtil:
    cmd: str
    argv: list

    def __init__(self, cmd: str, argv: List[str]) -> None:
        if len(argv) == 0:
            raise Exception("Not enough arguments.")

        self.cmd = cmd
        self.argv = argv

    def execute(self) -> None:
        if self.cmd == "command":
            cg = CommandGenerator(self.argv[0])
            cg.generate()
        elif self.cmd == "event":
            eg = EventGenerator(self.argv[0])
            eg.generate()
        elif self.cmd == "env":
            eg = EnvGenerator(self.argv[0])
            eg.generate()
        else:
            raise Exception(f"Generator invalid argument '{self.cmd}'")
