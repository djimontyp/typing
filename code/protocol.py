from typing import Protocol, runtime_checkable


class Proto(Protocol):
    def meth(self) -> int:
        ...


class C:
    def meth(self) -> int:
        return 0


def func(x: Proto) -> int:
    return x.meth()


func(C())  # Passes static type check

# ============================================================================

@runtime_checkable
class Closable(Protocol):
    def close(self):
        ...


assert isinstance(open("/some/file"), Closable)


@runtime_checkable
class Named(Protocol):
    name: str


import threading

assert isinstance(threading.Thread(name="Bob"), Named)
