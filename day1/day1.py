def read_file_as_list(file_name) -> list[str]:
    file = open(file_name)
    lines = file.readlines()
    return lines


def distance_between_lists():
    left_list, right_list = _split_left_right_lists()
    left_list.sort()
    right_list.sort()

    total_distance = sum(abs(right_list[i] - left_list[i]) for i, _ in enumerate(left_list))

    return total_distance


def similarity_score():
    left_list, right_list = _split_left_right_lists()

    score = sum(left * right_list.count(left) for left in left_list)

    return score


def _split_left_right_lists():
    original_list = read_file_as_list("day1_input.txt")
    left_list = []
    right_list = []
    for line in original_list:
        both = line.split("   ")
        left_list.append(int(both[0]))
        right_list.append(int(both[1]))
    return left_list, right_list
