import sys
import json
import random

from typing import List


def get_file(filename: str) -> str:
    """
    Get file content from given filename

    :param filename: name of the file
    :exception: File not found
    :return: file content
    """
    try:
        with open(filename, "r", encoding="latin-1") as file:
            file_content = file.read()
            file.close()
    except FileNotFoundError:
        print("ERROR: file doesn't exist")
        exit(84)
    return file_content


def add_mockup(content: List[dict]) -> None:
    """
    Add a field `note` with a random number between 0 and 10

    :param content: List of json object
    """
    ""
    rnd = random.Random()
    notes = [i for i in range(10)]

    for school in content:
        school["note"] = rnd.choice(notes)


def extract_fields_from_file(file: str) -> List[dict]:
    """
    CSV Supported : ['Roll_No', 'Off_Name', 'County', 'Ethos', 'xcoord', 'ycoord', 'Long', 'Lat']

    Algo :
        - Split array by line and by column
        - Transform all line into well formatted json
        - Push it to an List
    :param file: csv data
    :return: List of JSON with formatted fields
    """
    content = file.replace('"', '').split('\n')
    fields = [line.split(',') for line in content]
    legend = fields[0]
    schools = fields[1:]

    schools_dto: List[dict] = []
    for school in schools:
        if len(school) != len(legend):
            continue
        school_json = {}
        for i in range(len(legend)):
            school_json[legend[i]] = school[i]
        schools_dto.append(school_json)
    return schools_dto


def save_result(fields: List[dict]) -> None:
    with open("result.json", "w") as file:
        file.write('{\n"data": [')
        for school in fields:
            file.write(json.dumps(school, indent=4))
            file.write(',\n')
        file.write('{}\n]\n}')
        file.close()


def display_help() -> None:
    """ Display help """
    print("CSV ANALYZER")
    print("Options:")
    print("-m : create a random note column to mock result")
    print("-s : save the result into result.json file")
    print("Usage:")
    print("python3 mock-up-generator.py <file to parse> <options>")


def main(ac: int, av: List[str]) -> None:
    if ac == 0:
        display_help()
        exit(84)
    filename = av[0]
    file = get_file(filename)
    fields = extract_fields_from_file(file)
    if "-m" in av:
        add_mockup(fields)
    if "-s" in av:
        save_result(fields)
    else:
        for school in fields:
            print(json.dumps(school, indent=4))


if __name__ == '__main__':
    main(len(sys.argv[1:]), sys.argv[1:])
