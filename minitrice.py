from __future__ import annotations

import re
import sys
from decimal import Decimal, InvalidOperation, ROUND_HALF_UP, getcontext

getcontext().prec = 28
EXPR_RE = re.compile(r"^\s*(\d+(?:\.\d+)?)\s*([+\-*/])\s*(\d+(?:\.\d+)?)\s*$")


class EvaluationError(Exception):
    """L'expression n'est pas évaluable."""


class SyntaxError(EvaluationError):
    pass


class DivisionByZeroError(EvaluationError):
    pass


def format_result(value: Decimal) -> str:
    if value == value.to_integral():
        return str(value.quantize(Decimal(1)))
    quantized = value.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
    text = format(quantized.normalize())
    if "." in text:
        text = text.rstrip("0").rstrip(".")
    return text


def evaluate_expression(expr: str) -> str:
    match = EXPR_RE.match(expr)
    if not match:
        raise SyntaxError(f'Erreur de syntaxe pour le calcul: "{expr}"')

    left_raw, operator, right_raw = match.groups()
    try:
        left = Decimal(left_raw)
        right = Decimal(right_raw)
    except InvalidOperation as exc:
        raise SyntaxError(f'Erreur de syntaxe pour le calcul: "{expr}"') from exc

    if operator == "/" and right == 0:
        raise DivisionByZeroError("Division par zéro")

    operations = {
        "+": lambda x, y: x + y,
        "-": lambda x, y: x - y,
        "*": lambda x, y: x * y,
        "/": lambda x, y: x / y,
    }
    result = operations[operator](left, right)
    return format_result(result)


def main() -> int:
    interactive = sys.stdin.isatty()
    exit_code = 0

    while True:
        try:
            line = input("> " if interactive else "")
        except EOFError:
            if interactive:
                print("Fin des calculs")
            break

        if not line.strip():
            continue

        try:
            print(evaluate_expression(line))
        except DivisionByZeroError as error:
            print(error)
            exit_code = 1
            break
        except SyntaxError as error:
            print(error)
            exit_code = 1
            break

    return exit_code


if __name__ == "__main__":
    sys.exit(main())
