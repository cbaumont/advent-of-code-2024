from day1.day1 import read_file_as_list


def is_report_safe(report: list[int]):
    is_safe = False
    is_increasing = True
    is_decreasing = True

    for i in range(len(report) - 1):
        dif = report[i] - report[i + 1]
        if dif in range(1, 4) and is_decreasing:
            is_safe = True
            is_increasing = False
        elif dif in range(-1, -4, -1) and is_increasing:
            is_safe = True
            is_decreasing = False
        else:
            return False

    return is_safe


def count_safe_reports():
    raw_reports = read_file_as_list("inputs/day2_input.txt")

    reports = [[int(level) for level in raw_report.split(" ")] for raw_report in raw_reports]

    count = sum(1 for report in reports if is_report_safe(report))

    return count
