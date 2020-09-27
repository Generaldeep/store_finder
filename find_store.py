from docopt import docopt
import csv
import pandas as pd
import re

usage = '''

    Store Finder CLI.

    Usage:
        find_store --address="<address>"
        find_store --address="<address>" [--units=(mi|km)] [--output=text|json]
        find_store --zip=<zip>
        find_store --zip=<zip> [--units=(mi|km)] [--output=text|json]
'''


args = docopt(usage)


if args['--zip']:
    zip = args['--zip']
    units = args['--units']
    output = args['--output']

    matching_stores = []

    # read csv file
    df = pd.read_csv("store-locations.csv")

    # loop over csv file, return row(s) with matching zip code
    for index, row in df.iterrows():
        if row["Zip Code"]:
            split_zip = row['Zip Code'].replace('-', ' ').split(' ')
            if split_zip[0] == zip:  # write else to return the closest match
                matching_stores.append(row)

    print(matching_stores)

if args['--address']:
    store = args['--address']
    units = args['--units']
    output = args['--output']
