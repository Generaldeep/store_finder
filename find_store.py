from docopt import docopt
import csv
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
geolocator = Nominatim(user_agent="http")


def find_by_zip(zip, units, output):
    search = SearchEngine(simple_zipcode=True)
    input_zip_code_info = search.by_zipcode(zip)
    zip_lat = input_zip_code_info.lat
    zip_long = input_zip_code_info.lng

    distance_to_stores = []

    # read csv file
    stores = pd.read_csv("store-locations.csv")

    # loop over rows and find distance to all stores
    for index, row in stores.iterrows():
        distance = haversine((zip_lat, zip_long),
                             (row['Latitude'], row['Longitude']), unit=units)
        distance_to_stores.append({"dist": distance, "key": index, "row": row})

    sorted_list = sorted(distance_to_stores, key=lambda k: k['dist'])
    return sorted_list[0]


def find_by_address(address, units, output):
    # read csv file
    stores = pd.read_csv("store-locations.csv")
    location = geolocator.geocode(address)
    latitude = location.latitude
    longitude = location.longitude

    distance_to_stores = []

    # read csv file
    stores = pd.read_csv("store-locations.csv")

    # loop over rows and find distance to all stores
    for index, row in stores.iterrows():
        distance = haversine((latitude, longitude),
                             (row['Latitude'], row['Longitude']), unit=units)
        distance_to_stores.append({"dist": distance, "key": index, "row": row})

    sorted_list = sorted(distance_to_stores, key=lambda k: k['dist'])
    return sorted_list[0]


if args['--zip']:
    zip = args['--zip']
    units = args['--units'] or 'mi'
    return_output = args['--output'] or 'json'

    print(find_by_zip(zip, units, return_output))


if args['--address']:
    address = args['--address']
    units = args['--units'] or 'mi'
    return_output = args['--output'] or 'json'

    print(find_by_address(address, units, return_output))
