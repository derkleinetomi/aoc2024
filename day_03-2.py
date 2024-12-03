from pathlib import Path
import re


INPUT = Path("res/input_day_03-1.txt")


def main():
    data = []
    with open(INPUT, "r") as infile:
        data = infile.read()

    pattern = re.compile(r"(mul\(\d+,\d+\)|do\(\)|don't\(\))")
    matches = re.findall(pattern, data)

    relevant_matches = []
    include = True
    for match in matches:
        if str(match).startswith("don"):
            include = False
            continue
        if str(match).startswith("do("):
            include = True
            continue

        if include:
            relevant_matches.append(match)

    multiplication_results = []
    for match in relevant_matches:
        terms = match[4:-1]
        terms = terms.split(",")
        multiplication_results.append(int(terms[0]) * int(terms[1]))

    final_result = sum(multiplication_results)
    print(final_result)
if __name__ == "__main__":
    main()
