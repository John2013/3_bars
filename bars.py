import json
import sys
from math import radians, sin, cos, asin, sqrt


def load_data(filepath):
    with open(filepath, encoding='utf-8') as f:
        return json.load(f)


def get_biggest_bar(bars):
    biggest_bar = None
    max_seats_count = 0
    for bar in bars['features']:
        if bar['properties']['Attributes']['SeatsCount'] > max_seats_count:
            biggest_bar = bar
            max_seats_count = bar['properties']['Attributes']['SeatsCount']

    return biggest_bar


def get_smallest_bar(bars):
    smallest_bar = None
    min_seats_count = sys.maxsize
    for bar in bars['features']:
        if bar['properties']['Attributes']['SeatsCount'] < min_seats_count:
            smallest_bar = bar
            min_seats_count = bar['properties']['Attributes']['SeatsCount']

    return smallest_bar


def get_distance(latitude1, longitude1, latitude2, longitude2):
    """
    Вычисляет расстояние в километрах между двумя точками, учитывая окружность Земли.
    https://en.wikipedia.org/wiki/Haversine_formula
    """

    # convert decimal degrees to radians
    longitude1, latitude1, longitude2, latitude2 = map(radians, (longitude1, latitude1, longitude2, latitude2))

    # haversine formula
    dlongitude = longitude2 - longitude1
    dlatitude = latitude2 - latitude1
    a = sin(dlatitude / 2) ** 2 + cos(latitude1) * cos(latitude2) * sin(dlongitude / 2) ** 2
    c = 2 * asin(sqrt(a))
    km = 6367 * c
    return km


def get_closest_bar(bars, users_longitude, users_latitude):
    closest_bar = None
    min_distance = sys.float_info.max
    for bar in bars['features']:
        bars_longitude, bars_latitude = bar['geometry']['coordinates']
        distance = get_distance(users_longitude, users_latitude, bars_longitude, bars_latitude)
        if distance < min_distance:
            closest_bar = bar
            min_distance = distance

    return closest_bar


if __name__ == '__main__':
    longitude = float(input("Введите долготу: "))
    latitude = float(input("широту: "))
    path = "bars.json"
    bars = load_data(path)

    biggest_bar = get_biggest_bar(bars)
    smallest_bar = get_smallest_bar(bars)
    closest_bar = get_closest_bar(bars, longitude, latitude)

    print("Самый большой бар:", biggest_bar['properties']['Attributes']['Name'])
    print("Самый маленький бар:", smallest_bar['properties']['Attributes']['Name'])
    print("Ближайший бар:", closest_bar['properties']['Attributes']['Name'])
