import random
import statistics

def drunkman_path(steps, trials):
    distances_l=[]
    for _ in range(trials):
        origin_t=(0,0)
        current_coordinate_t=origin_t
        
        for _ in range(steps):
            delta_x, delta_y = random.choice([(0, 1), (0, -1), (1, 0), (-1, 0)])
            new_coordinate_x=current_coordinate_t[0]+delta_x
            new_coordinate_y=current_coordinate_t[1]+delta_y
            current_coordinate_t = (new_coordinate_x,new_coordinate_y)

        total_distance_x=current_coordinate_t[0]-origin_t[0]
        total_distance_y=current_coordinate_t[1]-origin_t[1]
        total_distance=((total_distance_x)**2+(total_distance_y)**2)**0.5

        distances_l.append(total_distance)
    
    distance_mean=statistics.mean(distances_l)
    distance_max=max(distances_l)
    distance_min=min(distances_l)

    return distance_mean, distance_max, distance_min

steps=5
trials=1000
d_m,d_max,d_min=drunkman_path(steps,trials)
print(f'random path of {steps} steps with {trials} trials')
print(f'Mean = {d_m}')
print(f'Max = {d_max}')
print(f'Min = {d_min}')
