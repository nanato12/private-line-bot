from abc import ABCMeta, abstractmethod
from ast import Constant, Expr


class BaseGenerator(metaclass=ABCMeta):
    ast_body: list

    def _ast_add_license(self) -> None:
        """append Expr to ast body"""

        with open("LICENSE") as license_file:
            self.ast_body.append(
                Expr(value=Constant(value=f"\n{license_file.read()}")),
            )

    @abstractmethod
    def generate(self) -> None:
        """generate py file"""
