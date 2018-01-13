import json
import sys

from os.path import isfile

from haversine import get_distance


def load_data(file_path: str):
    with open(file_path, encoding='utf-8') as file:
        return json.load(file)


def get_biggest_bar(bars: list):
    return max(
        bars,
        key=lambda bar: bar['properties']['Attributes']['SeatsCount']
    )


def get_smallest_bar(bars: list):
    return min(
        bars,
        key=lambda bar: bar['properties']['Attributes']['SeatsCount']
    )


def get_closest_bar(bars: list, users_longitude: float, users_latitude: float):
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
    if len(sys.argv) > 1 and isfile(sys.argv[1]):
        file_path = sys.argv[1]
    else:
        exit('Ошибка: Отсутствует путь к файлу или неверный путь к файлу')

    bars = load_data(file_path)['features']

    try:
        longitude = float(input('Введите долготу: '))
        latitude = float(input('широту: '))
    except ValueError:
        exit('Ошибка: введено некорректное число')

    biggest_bar = get_biggest_bar(bars)
    smallest_bar = get_smallest_bar(bars)
    closest_bar = get_closest_bar(bars, longitude, latitude)

    print(
        'Самый большой бар: {}\n'
        'Самый маленький бар: {}\n'
        'Ближайший бар: {}'.format(
            biggest_bar['properties']['Attributes']['Name'],
            smallest_bar['properties']['Attributes']['Name'],
            closest_bar['properties']['Attributes']['Name']
        )
    )
