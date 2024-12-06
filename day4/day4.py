from day1.day1 import read_file_as_list


def vertical_list(original_list: list[str]):
    vertical = []
    for i in range(len(original_list[0])):
        column = ""
        for line in original_list:
            column += line[i]
        vertical.append(column)

    return vertical


def diagonal_list(original_list: list[str]):
    result = []
    for col in range(len(original_list[0])):
        diagonal = ""
        for row in range(len(original_list) - (col - 1) - 1):
            diagonal += original_list[row][(col + row)]
        result.append(diagonal)

    return result


def all_diagonals(original_list: list[str]):
    result = []
    rows = len(original_list)
    cols = len(original_list[0])

    for col in range(cols):
        diagonal = ""
        for row in range(min(rows, cols - col)):
            diagonal += original_list[row][col + row]
        result.append(diagonal)

    for row in range(1, rows):
        diagonal = ""
        for col in range(min(cols, rows - row)):
            diagonal += original_list[row + col][col]
        result.append(diagonal)

    for col in range(cols):
        diagonal = ""
        for row in range(min(rows, col + 1)):
            diagonal += original_list[row][col - row]
        result.append(diagonal)

    for row in range(1, rows):
        diagonal = ""
        for col in range(min(cols, rows - row)):
            diagonal += original_list[row + col][cols - 1 - col]
        result.append(diagonal)

    return result


def reverse(original_list: list[str]):
    return [line[::-1] for line in original_list]


def check_xmas(original_list: list[str]):
    reverse_list = reverse(original_list)
    merged = original_list + reverse_list
    return sum(line.count("XMAS") for line in merged)


def count_xmas():
    original_list = read_file_as_list("inputs/day4_input.txt")
    vertical = vertical_list(original_list)
    diagonal = all_diagonals(original_list)
    return check_xmas(original_list) + check_xmas(vertical) + check_xmas(diagonal)
