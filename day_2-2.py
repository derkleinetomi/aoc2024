from pathlib import Path
from copy import deepcopy


INPUT = Path("res/input_day_2-1.txt")


def safe_with_dampener(dataset: list[int]) -> bool:
    dampened_datasets = dampened_reports(dataset)
    for dampened_dataset in dampened_datasets:
        dampened_dataset = zip(dampened_dataset[:-1], dampened_dataset[1:])
        dampened_dataset = list(dampened_dataset)

        no_immediate_duplicates = has_no_immediate_duplicates(dampened_dataset)
        allowed_step_sizes = has_allowed_step_sizes(dampened_dataset)
        unidirectionality = is_unidirectional(dampened_dataset)

        is_safe = all([no_immediate_duplicates, allowed_step_sizes, unidirectionality])
        if is_safe:
            return True
    return False


def dampened_reports(dataset: list[int]) -> list[list[int]]:
    dampened_sets = []
    for i in range(-1, len(dataset)):
        if i < 0:
            dampened_sets.append(dataset)
            continue
        this_set = deepcopy(dataset)
        this_set.pop(i)
        dampened_sets.append(this_set)
    return dampened_sets


def is_unidirectional(dataset) -> bool:
    direction = None
    for pair in dataset:
        current_direction = None
        if pair[0] < pair[1]:
            current_direction = "up"
        if pair[0] > pair[1]:
            current_direction = "down"
        if not direction:
            direction = current_direction
        if direction != current_direction:
            return False
    return True


def has_allowed_step_sizes(dataset) -> bool:
    if any([(pair[0] - pair[1]) ** 2 > 9 for pair in dataset]):
        return False
    return True


def has_no_immediate_duplicates(dataset: list[tuple[int, int]]) -> bool:
    if any([el[0] == el[1] for el in dataset]):
        return False
    return True


def main():
    data = []
    with open(INPUT, "r") as infile:
        data = infile.readlines()

    safe_reports = []
    for row in data:
        dataset = [int(el) for el in row.strip().split(" ")]
        if safe_with_dampener(dataset):
            safe_reports.append(dataset)

    print("total", len(data))
    print("safe", len(safe_reports))


if __name__ == "__main__":
    main()
