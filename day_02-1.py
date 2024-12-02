from pathlib import Path


INPUT = Path("res/input_day_2-1.txt")


def main():
    data = []
    with open(INPUT, "r") as infile:
        data = infile.readlines()

    unsafe_reports = []
    safe_reports = []
    for row in data:
        dataset = [int(el) for el in row.strip().split(" ")]

        zipped_dataset = list(zip(dataset[:-1], dataset[1:]))
        immediate_duplicates = any([el[0] == el[1] for el in zipped_dataset])
        if immediate_duplicates:
            unsafe_reports.append(dataset)
            continue

        unidirectional = True
        allowed_step_size = True
        direction = None
        for pair in zipped_dataset:
            if pair[0] < pair[1]:
                current_direction = "up"
            if pair[0] > pair[1]:
                current_direction = "down"
            if not direction:
                direction = current_direction
            if not direction == current_direction:
                unidirectional = False
            if ((pair[0] - pair[1]) ** 2) > 9:
                allowed_step_size = False
        if not unidirectional:
            unsafe_reports.append(dataset)
            continue
        if not allowed_step_size:
            unsafe_reports.append(dataset)
            continue
        safe_reports.append(dataset)

    print("total", len(data))
    print("unsafe", len(unsafe_reports))
    print("safe", len(safe_reports))

if __name__ == "__main__":
    main()
