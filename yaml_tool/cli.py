import argparse
import csv


def cli():
    parser = argparse.ArgumentParser(description="YAML Format")

    parser.add_argument(
        'filename',
        type=str,
        help="Enter file directory"
    )

    args = parser.parse_args()

    if not args.filename.lower().endswith('.csv'):
        print("{0} is not a CSV file".format(args.filename))
        exit()

    with open(args.filename, mode='rt') as f:
        read = csv.reader(f, delimiter=',')
        headers = next(read)
        division = headers.index('division')
        points = headers.index('points')
        sorter = sorted(read, key=lambda row: (
            int(row[division]), -int(row[points])))

    print("records:")
    for row in sorter[:3]:
        print("""- name: {0} {1}
  details: In division {2} from {3} performing {4}""".format(row[0], row[1], row[3], row[2], row[5]))
