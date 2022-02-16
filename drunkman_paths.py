import random

def drunkman_path(steps):
    origin=(0,0)
    current_coordinate=origin
    
    for _ in range(steps):
        delta_x, delta_y = random.choice([(0, 1), (0, -1), (1, 0), (-1, 0)])
        new_coordinate_x=current_coordinate[0]+delta_x
        new_coordinate_y=current_coordinate[1]+delta_y
        current_coordinate = (new_coordinate_x,new_coordinate_y)

    total_distance_x=current_coordinate[0]
    total_distance_y=current_coordinate[1]
    total_distance=((total_distance_x)**2+(total_distance_y)**2)**0.5

    return total_distance

d=drunkman_path(5)
print(d)
