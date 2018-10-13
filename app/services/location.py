from math import cos, asin, sqrt


# https://stackoverflow.com/questions/27928/calculate-distance-between-two-latitude-longitude-points-haversine-formula/21623206#21623206
# https://stackoverflow.com/questions/41336756/find-the-closest-latitude-and-longitude
def get_distance(lat1, lon1, lat2, lon2):
    """
    Calculate distance between lat1, lon1 and lat2, long2
    :param lat1: (float)
    :param lon1: (float)
    :param lat2: (float)
    :param lon2: (float)
    :return:
    """
    p = 0.017453292519943295
    a = 0.5 - cos((lat2-lat1)*p)/2 + cos(lat1*p)*cos(lat2*p) * (1-cos((lon2-lon1)*p)) / 2
    return 12742 * asin(sqrt(a))
