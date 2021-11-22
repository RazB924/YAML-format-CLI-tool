import argparse
import csv

parser = argparse.ArgumentParser(description="YAML Format")

parser.add_argument(
    'filename',
    type=str,
    help="Enter file directory"
)

args = parser.parse_args()
with open(args.filename, mode='rt') as f:
    read = csv.reader(f, delimiter=',')
    _ = next(read)
    sorter = sorted(read, key=lambda row: (int(row[3]), int(row[4])))
