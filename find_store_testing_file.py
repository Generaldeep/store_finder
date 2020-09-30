import csv
import json
import pandas as pd
from uszipcode import SearchEngine
from haversine import haversine, Unit
import pandas as pd
from haversine import haversine, Unit
from geopy.geocoders import Nominatim
from error_handler import UnAcceptedValueError


def find_by_zip(zip, units, output):
    # check if zip is 5 digits
    try:
        if(len(zip) < 5):
            raise UnAcceptedValueError(
                "Zip cannot be less than 5 digits")

    except UnAcceptedValueError as e:
        print("Received error:", e.data)

    # use uszipcode and get lat/long of input zip
    search = SearchEngine(simple_zipcode=True)
    input_zip_code_info = search.by_zipcode(zip)
    latitude = input_zip_code_info.lat
    longitude = input_zip_code_info.lng

    # call find_distance_to_stores
    result = find_distance_to_stores(latitude, longitude, units, output)
    return result


def find_by_address(address, units, output):
    # initiat geocoders instant
    geolocator = Nominatim(user_agent="http")
    # find lat/long of input address using geopy
    location = geolocator.geocode(address)

    latitude = location.latitude
    longitude = location.longitude

    # call find_distance_to_stores
    result = find_distance_to_stores(latitude, longitude, units, output)
    return result


def find_distance_to_stores(latitude, longitude, units, output):
    distance_of_zip_to_all_stores = []

    try:
        # read csv file
        stores = pd.read_csv("store-locations.csv")

        # loop over rows and find distance to all stores
        for index, row in stores.iterrows():
            distance = haversine((latitude, longitude),
                                 (row['Latitude'],
                                  row['Longitude']),
                                 unit=units)
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
