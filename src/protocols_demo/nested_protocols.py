from typing import Protocol

import attrs


dataclass = attrs.define(auto_attribs=True, frozen=True)


@dataclass
class Human(Protocol):
    attr1: str
    attr2: str


@dataclass
class GoodHuman(Human, Protocol):
    attr3: str


@dataclass
class BadHuman(Human, Protocol):
    attr4: str


class ImplementGoodHuman(GoodHuman): ...


class ImplementBadHuman(BadHuman): ...


ImplementGoodHuman()
ImplementBadHuman()


class CanJump(Protocol):
    def jump(self) -> None: ...


class CanSwim(Protocol):
    def smim(self) -> None: ...


class JumpoSwim(CanJump, CanSwim, Protocol): ...


class RealJumpoSmim(JumpoSwim): ...


RealJumpoSmim()
