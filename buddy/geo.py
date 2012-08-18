from geopy.point import Point
from geopy.distance import GreatCircleDistance as distance

def distance_two_points(lat1, lat2, long1, long2):
    p1 = Point(lat1, long2)
    p2 = Point(lat2, long2)

    return distance(p1, p2).miles


