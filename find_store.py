from docopt import docopt
import csv
import json
import pandas as pd
import re
from uszipcode import SearchEngine
from haversine import haversine, Unit
from geopy.geocoders import Nominatim


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
    # use uszipcode and get lat/long of input zip
    search = SearchEngine(simple_zipcode=True)
    input_zip_code_info = search.by_zipcode(zip)

    latitude = input_zip_code_info.lat
    longitude = input_zip_code_info.lng

    distance_of_zip_to_all_stores = []

    try:
        # read csv file
        stores = pd.read_csv("store-locations.csv")

        # loop over rows and find distance to all stores
        for index, row in stores.iterrows():
            distance = haversine((latitude, longitude),
                                 (row['Latitude'], row['Longitude']), unit=units)
            distance_of_zip_to_all_stores.append(
                {"dist": distance, "key": index, "Address": row['Address']})

        sorted_list = sorted(distance_of_zip_to_all_stores,
                             key=lambda k: k['dist'])

        if output == 'json':
            nearest_store = json.dumps(sorted_list[0])
        else:
            nearest_store = sorted_list[0]

        return nearest_store

    except Exception as ex:
        return ex


def find_by_address(address, units, output):
    # initiat geocoders instant
    geolocator = Nominatim(user_agent="http")
    # find lat/long of input address using geopy
    location = geolocator.geocode(address)

    latitude = location.latitude
    longitude = location.longitude

    distance_of_zip_to_all_stores = []

    try:
        # read csv file
        stores = pd.read_csv("store-locations.csv")

        # loop over rows and find distance to all stores
        for index, row in stores.iterrows():
            distance = haversine((latitude, longitude),
                                 (row['Latitude'], row['Longitude']), unit=units)
            distance_of_zip_to_all_stores.append(
                {"dist": distance, "key": index, "Address": row['Address']})

        # sort stores by distance
        sorted_list = sorted(distance_of_zip_to_all_stores,
                             key=lambda k: k['dist'])

        if output == 'json':
            nearest_store = json.dumps(sorted_list[0])
        else:
            nearest_store = sorted_list[0]

        return nearest_store

    except Exception as ex:
        return ex


if args['--zip']:
    zip = args['--zip']
    units = args['--units'] or 'mi'
    return_output = args['--output'] or 'text'

    print(find_by_zip(zip, units, return_output))


if args['--address']:
    address = args['--address']
    units = args['--units'] or 'mi'
    return_output = args['--output'] or 'text'

    print(find_by_address(address, units, return_output))
