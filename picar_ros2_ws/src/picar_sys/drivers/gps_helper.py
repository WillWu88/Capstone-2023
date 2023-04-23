from math import radians, cos, sin, asin, sqrt
import drivers.kf_constants

# keep sign
origin_lat = 0.0
origin_lon = 0.0

def abs_distance(lat1, lat2, lon1, lon2):
    # credit: https://www.geeksforgeeks.org/program-distance-two-points-earth/
    # The math module contains a function named
    # radians which converts from degrees to radians.
    lon1 = radians(lon1)
    lon2 = radians(lon2)
    lat1 = radians(lat1)
    lat2 = radians(lat2)
                                   
    # Haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * asin(sqrt(a))
                                                            
    # Radius of earth in kilometers. Use 3956 for miles
    r = 6371
    # calculate the result in meters
    return (c * r)/1000

def approx_distance(old, new):
    # longitude measurements in minutes
    return (new - old) * 1852

def origin_distance(label, new):
    if (lable):
        return approx_distance(origin_lat, new)
    else:
        return approx_distance(origin_lon, new)
    
def frame_transfer_x(angle, x, y):
    # first row of the rotation matrix
    # earth to body frame
    # up z, right hand rotation for positive angle
    # see doc for specific formula
    return cos(angle)*x - sin(angle)*y
