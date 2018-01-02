from math import radians, sin, cos, asin, sqrt


def get_distance(latitude1, longitude1, latitude2, longitude2):
    """
    Вычисляет расстояние в километрах между двумя точками, учитывая окружность
    Земли.
    https://en.wikipedia.org/wiki/Haversine_formula
    """
    EARTH_RADIUS = 6367

    # convert decimal degrees to radians
    longitude1, latitude1, longitude2, latitude2 = \
        map(radians, (longitude1, latitude1, longitude2, latitude2))

    # haversine formula
    difference_longitude = longitude2 - longitude1
    difference_latitude = latitude2 - latitude1
    a = sin(difference_latitude / 2) ** 2 + cos(latitude1) * cos(latitude2) * \
        sin(difference_longitude / 2) ** 2
    c = 2 * asin(sqrt(a))
    distance = EARTH_RADIUS * c
    return distance
