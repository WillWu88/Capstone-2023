# All navigation points:

origin_lat_deg = 38.0
origin_lat_min = 64.8417
origin_long_deg = -90.0
origin_long_min = -30.2358

is_turn_status = {
    "turn": 0,
    "heading_change": 1,
    "straight": 2
}

coord_label = {
    "lat": 0,
    "long": 1
}

point_q = []
is_turn_q = []

p1_lat_min = 64.8670
p1_long_min = -30.2331
# p1_lat_min = 15.
# p1_long_min = -0.5
point_q.append([p1_lat_min, p1_long_min])
is_turn_q.append(is_turn_status["turn"])

# Turn 1

p2_lat_min = 64.8664
p2_long_min = -30.2071
point_q.append([p2_lat_min, p2_long_min])
is_turn_q.append(is_turn_status["heading_change"])


p3_lat_min = 64.8588
p3_long_min = -30.1743
point_q.append([p3_lat_min, p3_long_min])
is_turn_q.append(is_turn_status["turn"])

# Turn 2

p4_lat_min = 64.8471
p4_long_min = -30.1831
point_q.append([p4_lat_min, p4_long_min])
is_turn_q.append(is_turn_status["heading_change"])

p5_lat_min = 64.8345
p5_long_min = -30.1891
point_q.append([p5_lat_min, p5_long_min])
is_turn_q.append(is_turn_status["turn"])

# Turn 3

p6_lat_min = 64.8346
p6_long_min = -30.1935
point_q.append([p6_lat_min, p6_long_min])
is_turn_q.append(is_turn_status["heading_change"])

# Go to origin
p7_lat_min = 64.8346
p7_long_min = -30.1935
point_q.append([p6_lat_min, p6_long_min])
is_turn_q.append(is_turn_status["straight"])


