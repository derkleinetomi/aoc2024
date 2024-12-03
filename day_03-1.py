from pathlib import Path
import re


INPUT = Path("res/input_day_03-1.txt")


def main():
    data = []
    with open(INPUT, "r") as infile:
        data = infile.read()

    pattern = re.compile(r"mul\(\d+,\d+\)")
    matches = re.findall(pattern, data)

    multiplication_results = []
    for match in matches:
        terms = match[4:-1]
        terms = terms.split(",")
        multiplication_results.append(int(terms[0]) * int(terms[1]))

    final_result = sum(multiplication_results)
    print(final_result)

if __name__ == "__main__":
    main()
