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

  # With a conventional if statement. Sad, can't avoid mutation and repetition.
  # Also awkwardly can't declare the type more than once.
  if argAsInt < 10:
    output2: str = 'Less than 10'
  else:
    output2 = 'Not less than 10'
  print(output2)

  # Could wrap the if in a function so the value can be returned as though it's
  # an expression
  def checkIt(n: int) -> str:
    if argAsInt < 10:
      return 'Less than 10'
    else:
      return 'Not less than 10'
  output3: str = checkIt(int(sys.argv[1]))
  print(output3)


if __name__ == '__main__': main()
