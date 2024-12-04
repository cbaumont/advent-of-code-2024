import re

from day1.day1 import read_file_as_list


def find_multiply_operations(corrupted: str):
    multiply_operations = re.findall(r"mul\(\d\d?\d?,\d\d?\d?\)", corrupted)
    return multiply_operations


def find_all_operations(corrupted: str):
    all_operations = re.findall(r"mul\(\d\d?\d?,\d\d?\d?\)|do\(\)|don't\(\)", corrupted)
    return all_operations


def multiply(operation: str) -> int:
    split = operation.split(",")
    number_a = int(split[0][4:])
    number_b = int(split[1].split(")")[0])
    return number_a * number_b


def multiply_with_commands(operations_list: list):
    acc = 0
    command = "do()"
    for operation in operations_list:
        if operation == "don't()" or operation == "do()":
            command = operation
            continue
        if command != "don't()":
            acc += multiply(operation)

    return acc


def multiplications_sum():
    corrupted_list = read_file_as_list("inputs/day3_input.txt")

    operations_lists = [find_multiply_operations(corrupted) for corrupted in corrupted_list]

    result_1 = sum(multiply(operation) for operation_list in operations_lists for operation in operation_list)

    all_operations_list = [find_all_operations(corrupted) for corrupted in corrupted_list]

    result_2 = sum(multiply_with_commands(all_operations) for all_operations in all_operations_list)

    return result_2
