from day1.day1 import read_file_as_list


def remove_item(original_list: list[int], index: int) -> list[int]:
    modified_list = original_list[:]
    modified_list.pop(index)

    return modified_list


def is_report_safe(report: list[int], is_increasing: bool = True, is_decreasing: bool = True):
    if len(report) <= 1: return True

    dif = report[0] - report[1]
    if dif in range(1, 4) and is_decreasing:
        return is_report_safe(remove_item(report, 0), False, True)
    if dif in range(-1, -4, -1) and is_increasing:
        return is_report_safe(remove_item(report, 0), True, False)

    return False


def is_report_safe_problem_dampener(report: list[int]):
    if is_report_safe(report):
        return True

    for i in range(len(report)):
        if is_report_safe(remove_item(report, i)):
            return True

    return False


def count_safe_reports():
    raw_reports = read_file_as_list("inputs/day2_input.txt")

    reports = [[int(level) for level in raw_report.split(" ")] for raw_report in raw_reports]

    count = sum(1 for report in reports if is_report_safe_problem_dampener(report))

    return count
