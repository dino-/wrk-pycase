#! /usr/bin/env python3

import sys

sys.path.insert(0, 'lib')

# pylint: disable=wrong-import-position
from Control.Case import case, const, otherwise


def main() -> None:
  argAsInt = int(sys.argv[1])

  # With the case expression code
  output1: str = case(argAsInt,
    [ (lambda n: n < 10, const('Less than 10'))
    , (otherwise       , const('Not less than 10'))
    ])
  print(output1)

  # Using a conventional if statement. Unfortunately, because if is a statement
  # and not an expression, we can't avoid mutation and repetition. Also,
  # awkwardly can't include a type signature more than once, mypy rejects it.
  if argAsInt < 10:
    output2: str = 'Less than 10'
  else:
    output2 = 'Not less than 10'
  print(output2)

  # We could wrap the if in a function so the value can be returned as though
  # it's an expression, but this is awkward too. Single assignment though!
  def checkIt(n: int) -> str:
    if argAsInt < 10:
      return 'Less than 10'
    else:
      return 'Not less than 10'
  output3: str = checkIt(argAsInt)
  print(output3)

  # For either/or two-choice decisions like this, I'd probably use the ternary
  # expression.
  output4: str = 'Less than 10' if argAsInt < 10 else 'Not less than 10'
  print(output4)


if __name__ == '__main__': main()
