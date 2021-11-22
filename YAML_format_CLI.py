import argparse
import csv

parser = argparse.ArgumentParser(description="YAML Format")

parser.add_argument(
    'filename',
    type=str,
    help="Enter file directory"
)

args = parser.parse_args()

# Checks whether the file is a CSV file, if it isn't the program will end
# Comment the 3 lines out if file type doesn't matter
if not args.filename.lower().endswith('.csv'):
    print("{0} is not a CSV file".format(args.filename))
    exit()

# Opens and reads the CSV file
# The records are sorted by division in asecending order and then points in descending order if there is a tie
# The code can sort by division and points even if the column  position is not defined
with open(args.filename, mode='rt') as f:
    read = csv.reader(f, delimiter=',')
    headers = next(read)
    division = headers.index('division')
    points = headers.index('points')
    sorter = sorted(read, key=lambda row: (
        int(row[division]), -int(row[points])))

# Prints the top 3 records in YAML format
print("records:")
for row in sorter[:3]:
    print("""- name: {0} {1}
  details: In division {2} from {3} performing {4}""".format(row[0], row[1], row[3], row[2], row[5]))
