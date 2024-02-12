from typing import Protocol

import attrs


dataclass = attrs.define(auto_attribs=True, frozen=True)


@dataclass
class ExplicitBaseA(Protocol):
    attr1: str
    attr2: str

    attr_with_default: int = 15

    def method(self) -> str: ...

    def method_with_default(self) -> str:
        return "default"


@dataclass
class ImplementsExplicitBaseA(ExplicitBaseA): ...


ImplementsExplicitBaseA()
