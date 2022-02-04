from typing import Callable, TypeVar

__all__ = ['case', 'const', 'otherwise']


a = TypeVar('a')
b = TypeVar('b')


# FIXME Should live in Data.Function
def const(y: b) -> Callable[[a], b]:
  return lambda _: y


Case = tuple[Callable[[a], bool], Callable[[a], b]]
Cases = list[Case[a, b]]


def case(val: a, cases: Cases[a, b]) -> b:
  # Filter the cases for the ones whose predicate matches given the value and
  # take the first one
  matchedCase: Case[a, b] = list(filter(lambda t: t[0](val), cases))[0]

  # Isolate the function to be performed (the right side of the tuple, or
  # element 1)
  matchedCaseFunc: Callable[[a], b] = matchedCase[1]

  # Call it on the value and return the result
  return matchedCaseFunc(val)


# A predicate that always succeeds regardless of the input, for the
# fall-through case
otherwise: Callable[[a], bool] = const(True)
