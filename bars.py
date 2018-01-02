import json

from haversine import get_distance

import sys


def load_data(filepath):
    with open(filepath, encoding='utf-8') as f:
        return json.load(f)


def get_biggest_bar(bars):
    max_seats_count = max([bar['properties']['Attributes']['SeatsCount'] for bar in bars['features']])

    for bar in bars['features']:
        if bar['properties']['Attributes']['SeatsCount'] == max_seats_count:
            return bar


def get_smallest_bar(bars):
    min_seats_count = min([bar['properties']['Attributes']['SeatsCount'] for bar in bars['features']])

    for bar in bars['features']:
        if bar['properties']['Attributes']['SeatsCount'] == min_seats_count:
            return bar


def get_closest_bar(bars, users_longitude, users_latitude):
    for bar in bars['features']:
        bar['geometry']['distance'] = get_distance(
            bar['geometry']['coordinates'][0],
            bar['geometry']['coordinates'][1],
            users_longitude,
            users_latitude
        )
    min_distance = min([bar['geometry']['distance'] for bar in bars['features']])
    for bar in bars['features']:
        if bar['geometry']['distance'] == min_distance:
            return bar


if __name__ == '__main__':
    if len(sys.argv) > 1:
        file_path = sys.argv[1]
    else:
        file_path = input("Введите путь до файла с данными о барах: ")

    bars = load_data(file_path)
    longitude = float(input("Введите долготу: "))
    latitude = float(input("широту: "))

    biggest_bar = get_biggest_bar(bars)
    smallest_bar = get_smallest_bar(bars)
    closest_bar = get_closest_bar(bars, longitude, latitude)

    print("Самый большой бар:", biggest_bar['properties']['Attributes']['Name'])
    print("Самый маленький бар:", smallest_bar['properties']['Attributes']['Name'])
    print("Ближайший бар:", closest_bar['properties']['Attributes']['Name'])
