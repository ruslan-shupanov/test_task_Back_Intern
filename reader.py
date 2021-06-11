import csv


def read_csv(file_csv):
    """Read the given csv file and return its data in dictionary format."""
    data = {}
    with open(file_csv) as tmp_csv:
        dict_csv = csv.DictReader(tmp_csv)
        for row in dict_csv:
            key = int(row['Id'])
            data[key] = row
    return data
