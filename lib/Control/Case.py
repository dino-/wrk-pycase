from typing import Callable, Generic, TypeVar


A = TypeVar('A')
B = TypeVar('B')


# FIXME Should live in Data.Function
def const(b: B) -> Callable[[A], B]:
  return lambda _: b

Case = tuple[Callable[[A], bool], Callable[[A], B]]
Cases = list[Case[A, B]]

def case(val: A, cases: Cases[A, B]) -> B:
  matchedCaseFunc = (list(filter(lambda t: t[0](val), cases))[0])[1]
  return matchedCaseFunc(val)


otherwise: Callable[[A], bool] = const(True)
