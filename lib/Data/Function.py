from typing import Callable, TypeVar


a = TypeVar('a')
b = TypeVar('b')


def const(y: b) -> Callable[[a], b]:
  return lambda _: y
