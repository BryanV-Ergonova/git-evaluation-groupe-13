from __future__ import annotations

import random
import sys
from typing import List

OPERATORS = ["+", "-", "*", "/"]


def parse_count(args: List[str]) -> int:
    if len(args) != 1:
        raise ValueError("Usage: ./generator <count>")
    try:
        count = int(args[0])
    except ValueError as exc:
        raise ValueError("Le paramètre <count> doit être un entier positif") from exc
    if count <= 0:
        raise ValueError("Le paramètre <count> doit être strictement positif")
    return count


def main() -> int:
    try:
        count = parse_count(sys.argv[1:])
    except ValueError as error:
        print(error, file=sys.stderr)
        return 1

    for _ in range(count):
        left = random.randint(1, 1000)
        right = random.randint(1, 1000)
        operator = random.choice(OPERATORS)
        print(f"{left}{operator}{right}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
