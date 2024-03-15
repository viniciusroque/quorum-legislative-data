import csv
from typing import Iterator


def parse_csv(file_path) -> Iterator[dict]:
    with open(file_path, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            yield row
