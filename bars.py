import json
import sys

from os.path import isfile

from haversine import get_distance


def load_data(file_path: str):
    with open(file_path, encoding='utf-8') as file:
        return json.load(file)


def get_biggest_bar(bars: dict):
    return max(
        bars,
        key=lambda bar: bar['properties']['Attributes']['SeatsCount'])


def get_smallest_bar(bars: dict):
    return min(
        bars,
        key=lambda bar: bar['properties']['Attributes']['SeatsCount'])


def get_closest_bar(bars: dict, users_longitude: float, users_latitude: float):
    return min(
        bars,
        key=lambda bar: get_distance(
            bar['geometry']['coordinates'][0],
            bar['geometry']['coordinates'][1],
            users_longitude,
            users_latitude
        )
    )


if __name__ == '__main__':
    file_path = ""
    if len(sys.argv) > 1 and isfile(sys.argv[1]):
        file_path = sys.argv[1]
    else:
        exit("Ошибка: Отсутствует путь к файлу или неверный путь к файлу")

    bars = load_data(file_path)['features']

    longitude = input("Введите долготу: ")
    if not longitude.isdigit():
        exit("Ошибка: ожидается число, введено " + longitude)
    latitude = input("широту: ")
    if not longitude.isdigit():
        exit("Ошибка: ожидается число, введено " + latitude)

    longitude, latitude = float(longitude), float(latitude)

    biggest_bar = get_biggest_bar(bars)
    smallest_bar = get_smallest_bar(bars)
    closest_bar = get_closest_bar(bars, longitude, latitude)

    print(
        "Самый большой бар:",
        biggest_bar['properties']['Attributes']['Name']
    )
    print(
        "Самый маленький бар:",
        smallest_bar['properties']['Attributes']['Name']
    )
    print(
        "Ближайший бар:",
        closest_bar['properties']['Attributes']['Name']
    )
