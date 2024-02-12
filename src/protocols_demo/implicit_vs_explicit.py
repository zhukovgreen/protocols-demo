from typing import Protocol

import attrs


dataclass = attrs.define(auto_attribs=True, frozen=True)


@dataclass
class ExplicitBaseA(Protocol):
    attr1: str
    attr2: str

    def method(self, a: str) -> int: ...


@dataclass
class ImplicitBaseA(Protocol):
    attr3: str
    attr4: str


@dataclass
class ImplementsImplicitBaseA: ...


ImplementsImplicitBaseA()


@dataclass
class ImplementsExplicitBaseA(ExplicitBaseA): ...


ImplementsExplicitBaseA()
