
import sys
import csv
import argparse


def get_args():
    """
    Command line input arguments defined
    Returns
    -------
    parser.parse_args()
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('--aweber-csv', required=True)
    parser.add_argument('--emails', required=True)
    parser.add_argument('--out-csv-file',
                        default=sys.stdout,
                        type=argparse.FileType('w')
                        )
    return parser.parse_args()


output_fields = [
    'email',
    'date_subscribed',
    'lead_source',
    'lead_medium',
    'lead_campaign',
    'lead_term',
    'lead_content',
]

if __name__ == '__main__':
    args = get_args()
    reader = csv.DictReader(
        open(args.aweber_csv)
    )
    print(f" reader type: {type(reader)}")
    with open(args.emails) as handle:
        emails = set(line.strip() for line in handle)
    emails_iter = iter(emails)
    print(next(emails_iter))
    print(next(emails_iter))
    writer = csv.DictWriter(
        args.out_csv_file,
        fieldnames=output_fields
    )
    print(f" writer type: {type(writer)}")

    # wr = writer.writeheader()
    # print(f"writer return on writeheader: {wr}")
    print("")
    for row in reader:
        if row['Email'] in emails:
            row['email'] = row['Email']
            writer.writerow({
                field: row[field]
                for field in output_fields
           })
