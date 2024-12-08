# Day 2: Red-Nosed Reports
from itertools import pairwise


def is_report_safe(report: list[int]) -> bool:
    increasing = all(x < y for x, y in pairwise(report))
    decreasing = all(x > y for x, y in pairwise(report))
    gradual_movement = all(1 <= abs(x - y) <= 3 for x, y in pairwise(report))

    return (increasing or decreasing) and gradual_movement


def is_report_safe_after_problem_dampener(report: list[int]) -> bool:
    dampened_reports = [report[:x] + report[x+1:] for x, level in enumerate(report)]

    return any(is_report_safe(report) for report in dampened_reports)


def count_safe_reports(data: str) -> None:
    safe_reports = 0

    with open(data, encoding="utf-8") as input:
        for report in input:
            report = [int(level) for level in report.split()]
            if is_report_safe(report) or is_report_safe_after_problem_dampener(report):
                safe_reports += 1

    print(f"There are {safe_reports} safe reports.")


if __name__ == "__main__":
    count_safe_reports("input.txt")
