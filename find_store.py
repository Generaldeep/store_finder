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


def find_by_zip(zip, units, output):
    matching_stores = []
    # read csv file
    stores = pd.read_csv("store-locations.csv")

    # loop over csv file, return row(s) with matching zip code
    for index, row in stores.iterrows():
        if row["Zip Code"]:
            split_zip = row['Zip Code'].replace('-', ' ').split(' ')
            if split_zip[0] == zip:  # write else to return the closest match
                matching_stores.append(row)

    return matching_stores


if args['--zip']:
    zip = args['--zip']
    units = args['--units']
    return_output = args['--output']

    find_matching_store = find_by_zip(zip, units, return_output)

    if len(find_matching_store) > 0:
        print(find_matching_store)
    else:
        print('not found')

if args['--address']:
    store = args['--address']
    units = args['--units']
    output = args['--output']
