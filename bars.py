import json
import sys

from haversine import get_distance


def load_data(file_path):
    with open(file_path, encoding='utf-8') as file:
        return json.load(file)


def get_biggest_bar(bars):
    return max(bars['features'], key=lambda bar: bar['properties']['Attributes']['SeatsCount'])


def get_smallest_bar(bars):
    return min(bars['features'], key=lambda bar: bar['properties']['Attributes']['SeatsCount'])


# Спасибо проверяющим из devman.org что намекнули на потрясный функционал min и max функций, не знал о нём.
# С Новым Годом вас!

def get_closest_bar(bars, users_longitude, users_latitude):
    for bar in bars['features']:
        bar['geometry']['distance'] = get_distance(
            bar['geometry']['coordinates'][0],
            bar['geometry']['coordinates'][1],
            users_longitude,
            users_latitude
        )

    return min(bars['features'], key=lambda bar: bar['geometry']['distance'])


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
