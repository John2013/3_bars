from math import radians, sin, cos, asin, sqrt

EARTH_RADIUS = 6367


def get_distance(latitude1: float, longitude1: float, latitude2: float,
                 longitude2: float) -> float:
    """
    Вычисляет расстояние в километрах между двумя точками, учитывая окружность
    Земли.
    https://en.wikipedia.org/wiki/Haversine_formula
    """

    longitude1, latitude1, longitude2, latitude2 = \
        map(radians, (longitude1, latitude1, longitude2, latitude2))

    difference_longitude = longitude2 - longitude1
    difference_latitude = latitude2 - latitude1
    a = sin(difference_latitude / 2) ** 2 + cos(latitude1) * cos(latitude2) * \
        sin(difference_longitude / 2) ** 2
    c = 2 * asin(sqrt(a))
    distance = EARTH_RADIUS * c
    return distance
