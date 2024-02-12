from typing import Callable, Protocol


class ComplexCallableLike(Protocol):
    @staticmethod
    def __call__(a: str, *, kwarg1: int) -> float: ...


def foo(self, a: str, *, kwarg1: int): ...


foo_like_callable: Callable[[str, int], float]
foo_like_protocol: ComplexCallableLike

foo_like_callable()
foo_like_protocol()
