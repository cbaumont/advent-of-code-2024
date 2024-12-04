import re

from day1.day1 import read_file_as_list


def find_multiply_operations(corrupted: str):
    multiply_functions = re.findall(r"mul\(\d\d?\d?,\d\d?\d?\)", corrupted)
    return multiply_functions


def multiply(operation: str) -> int:
    split = operation.split(",")
    number_a = int(split[0][4:])
    number_b = int(split[1].split(")")[0])
    return number_a * number_b


def multiplications_sum():
    corrupted_list = read_file_as_list("inputs/day3_input.txt")

    operations_lists = [find_multiply_operations(corrupted) for corrupted in corrupted_list]

    result = sum(multiply(operation) for operation_list in operations_lists for operation in operation_list)

    return result
