# Day 3: Mull It Over
import re


def parse_corrupted_data(data: str) -> None:
    corrupted_data = ""
    results = 0

    valid_instruction = re.compile(
        r"""
        mul\(                           # Start of valid instruction
        (?P<x>\d{1,3})                  # First number
        ,                               # Comma delimiter
        (?P<y>\d{1,3})                  # Second number
        \)                              # End of valid instruction
        """,
        re.VERBOSE,
    )

    with open(data, encoding="utf-8") as input:
        corrupted_data = input.read()

    for instruction in valid_instruction.finditer(corrupted_data):
        numbers = instruction.groupdict()
        results += int(numbers["x"]) * int(numbers["y"])

    print(results)


if __name__ == "__main__":
    parse_corrupted_data("input.txt")
