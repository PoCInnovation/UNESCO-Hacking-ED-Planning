import sys
import csv
import json
import random

from typing import List


def display_help() -> None:
    """ Display help """
    print("CSV ANALYZER")
    print("Options:")
    print("-m : create a random note column to mock result")
    print("Usage:")
    print("python3 mock-up-generator.py <file to parse> <output file> <options>")


def main(ac: int, av: List[str]) -> None:
    if ac < 2:
        display_help()
        exit(84)

    data = {}
    with open(av[0]) as csvFile:
        rnd = random.Random()
        notes = [i for i in range(10)]

        csv_reader = csv.DictReader(csvFile)
        for rows in csv_reader:
            if "-m" in av:
                rows["note"] = str(rnd.choice(notes))
            data[rows["Roll_No"]] = rows

    with open(av[1], "w") as jsonFile:
        jsonFile.write(json.dumps(data, indent=4))


if __name__ == '__main__':
    main(len(sys.argv[1:]), sys.argv[1:])
