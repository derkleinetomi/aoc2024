from pathlib import Path


INPUT = Path("res/input_day_1-1.txt")


def main():
    data = []
    with open(INPUT, "r") as infile:
        data = infile.readlines()

    list_one = []
    list_two = []

    for row in data:
        row = row.strip().split(" ")
        list_one.append(row[0])
        list_two.append(row[-1])

    list_one.sort()
    list_two.sort()

    sorted_and_zipped = zip(list_one, list_two)

    distances = []

    for pair in sorted_and_zipped:
        distance = int(pair[0]) - int(pair[1])
        if distance < 0:
            distance = distance * -1

        distances.append(distance)

    print(sum(distances))

if __name__ == "__main__":
    main()
