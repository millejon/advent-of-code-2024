# Day 3: Mull It Over
import re


def parse_corrupted_data(data: str) -> None:
    corrupted_data = ""
    results = 0
    enabled = True

    valid_instructions = re.compile(
        r"""
        do\(\) |
        don't\(\) |
        mul\(                           # Start of valid multiply instruction
        (?P<x>\d{1,3})                  # First number
        ,                               # Comma delimiter
        (?P<y>\d{1,3})                  # Second number
        \)                              # End of valid multiply instruction
        """,
        re.VERBOSE,
    )

    with open(data, encoding="utf-8") as input:
        corrupted_data = input.read()

    for instruction in valid_instructions.finditer(corrupted_data):
        if instruction.group() == "do()":
            enabled = True
        elif instruction.group() == "don't()":
            enabled = False
        elif enabled:
            numbers = instruction.groupdict()
            results += int(numbers["x"]) * int(numbers["y"])

    print(results)


if __name__ == "__main__":
    parse_corrupted_data("input.txt")
