from math import radians, sin, cos, asin, sqrt


def get_distance(
    latitude1: float,
    longitude1: float,
    latitude2: float,
    longitude2: float
) -> float:
    longitude1, latitude1, longitude2, latitude2 = map(
        radians,
        (
            longitude1,
            latitude1,
            longitude2,
            latitude2
        )
    )
    earth_radius = 6367
    difference_longitude = longitude2 - longitude1
    difference_latitude = latitude2 - latitude1
    a = sin(difference_latitude / 2) ** 2 + cos(latitude1) * cos(latitude2) * \
        sin(difference_longitude / 2) ** 2
    # Backslashes may still be appropriate at times. For example, long,
    # multiple with-statements cannot use implicit continuation, so backslashes
    # are acceptable
    # https://www.python.org/dev/peps/pep-0008/#id19
    # не вижу здесь способа написания без обратного слеша
    c = 2 * asin(sqrt(a))
    distance = earth_radius * c
    return distance
