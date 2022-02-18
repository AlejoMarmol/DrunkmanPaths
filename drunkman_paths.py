import random

def drunkman_path(steps):
    origin_t=(0,0)
    current_coordinate_t=origin_t
    
    for _ in range(steps):
        delta_x, delta_y = random.choice([(0, 1), (0, -1), (1, 0), (-1, 0)])
        new_coordinate_x=current_coordinate_t[0]+delta_x
        new_coordinate_y=current_coordinate_t[1]+delta_y
        current_coordinate_t = (new_coordinate_x,new_coordinate_y)

    total_distance_x=current_coordinate_t[0]
    total_distance_y=current_coordinate_t[1]
    total_distance=((total_distance_x)**2+(total_distance_y)**2)**0.5

    return total_distance

d=drunkman_path(10)
print(d)
