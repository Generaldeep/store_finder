from docopt import docopt
import csv
import pandas as pd
import re
from uszipcode import SearchEngine
from haversine import haversine, Unit


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


def find_nearest_store(zip, unit, output):
    search = SearchEngine(simple_zipcode=True)
    input_zip_code_info = search.by_zipcode(zip)
    zip_lat = input_zip_code_info.lat
    zip_long = input_zip_code_info.lng

    distance_to_stores = []

    # read csv file
    stores = pd.read_csv("store-locations.csv")

    # loop over rows and find distance to all stores
    for index, row in stores.iterrows():
        test = row
        distance = haversine((zip_lat, zip_long),
                             (row['Latitude'], row['Longitude']), unit=unit)
        distance_to_stores.append({"dist": distance, "key": index, "row": row})

    sorted_list = sorted(distance_to_stores, key=lambda k: k['dist'])
    return sorted_list[0]


if args['--zip']:
    zip = args['--zip']
    units = args['--units']
    return_output = args['--output']

    find_matching_store = find_by_zip(zip, units, return_output)

    if len(find_matching_store) > 0:
        print(find_matching_store)
    else:
        print(find_nearest_store(zip, units, return_output))

if args['--address']:
    store = args['--address']
    units = args['--units']
    output = args['--output']
