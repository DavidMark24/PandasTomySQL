import csv


def read_csv(file):
    data = []
    with open(file, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            data.append(row)
    return data
