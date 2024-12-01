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

    location_id_frequency_products = []

    for location_id in list_one:
        location_id_frequency_products.append(int(location_id) * list_two.count(location_id))

    print(sum(location_id_frequency_products))


if __name__ == "__main__":
    main()
