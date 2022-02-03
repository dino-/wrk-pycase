#! /usr/bin/env python3

import sys

sys.path.insert(0, 'lib')

# pylint: disable=wrong-import-position
from Control.Case import case, const, otherwise


def main() -> None:
  output: str = case(int(sys.argv[1]),
    [ (lambda n: n < 10, const('Less than 10'))
    , (otherwise       , const('Not less than 10'))
    ])
  print(output)


if __name__ == '__main__': main()
