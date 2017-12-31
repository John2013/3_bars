import json
import sys

from math import radians, sin, cos, asin, sqrt


def load_data(filepath):
    with open(filepath, encoding='utf-8') as f:
        return json.load(f)


def get_biggest_bar(data):
    biggest_bar = None
    max_seats_count = 0
    for bar_ in data['features']:
        if bar_['properties']['Attributes']['SeatsCount'] > max_seats_count:
            biggest_bar = bar_
            max_seats_count = bar_['properties']['Attributes']['SeatsCount']

    return biggest_bar


def get_smallest_bar(data):
    smallest_bar = None
    min_seats_count = sys.maxsize
    for bar_ in data['features']:
        if bar_['properties']['Attributes']['SeatsCount'] < min_seats_count:
            smallest_bar = bar_
            min_seats_count = bar_['properties']['Attributes']['SeatsCount']

    return smallest_bar


def haversine(lat1, lon1, lat2, lon2):
    """
    Вычисляет расстояние в километрах между двумя точками, учитывая окружность Земли.
    https://en.wikipedia.org/wiki/Haversine_formula
    """

    # convert decimal degrees to radians
    lon1, lat1, lon2, lat2 = map(radians, (lon1, lat1, lon2, lat2))

    # haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * asin(sqrt(a))
    km = 6367 * c
    return km


def get_closest_bar(data, lon1, lat1):
    closest_bar = None
    min_distance = sys.float_info.max
    for bar_ in data['features']:
        lon2, lat2 = bar_['geometry']['coordinates']
        distance = haversine(lon1, lat1, lon2, lat2)
        if distance < min_distance:
            closest_bar = bar_
            min_distance = distance

    return closest_bar


if __name__ == '__main__':
    lon = float(input("Введите долготу: "))
    lat = float(input("широту: "))
    path = "bars.json"
    data = load_data(path)

    biggest_bar = get_biggest_bar(data)
    smallest_bar = get_smallest_bar(data)
    closest_bar = get_closest_bar(data, lon, lat)

    print("Самый большой бар:", biggest_bar['properties']['Attributes']['Name'])
    print("Самый маленький бар:", smallest_bar['properties']['Attributes']['Name'])
    print("Ближайший бар:", closest_bar['properties']['Attributes']['Name'])
