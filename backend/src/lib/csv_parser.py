import csv
from typing import Any, Iterator


def parse_csv(file_path) -> Iterator[tuple[int, dict[str, Any]]]:
    with open(file_path, "r") as file:
        reader = csv.DictReader(file)
        for line_number, row in enumerate(reader, start=2):
            yield line_number, row
