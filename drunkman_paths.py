import random
import statistics
from bokeh.plotting import figure, show
# from bokeh.layouts import gridplot
# from bokeh.io import export_png

# import numpy as np

def drunkman_paths(n_steps, n_trials, n_graphs):
    distances_l=[]
    i_graph_l=random.sample(range(0,trials),n_graphs) #remember to handle error
    print(i_graph_l)
    for j in range(n_trials):
        coordinates_x_l=[]
        coordinates_y_l=[]
        origin_t=(0,0)
        current_coordinate_t=origin_t
        coordinates_x_l.append(origin_t[0])
        coordinates_y_l.append(origin_t[1])
        
        for _ in range(n_steps):
            delta_x, delta_y = random.choice([(0, 1), (0, -1), (1, 0), (-1, 0)])
            new_coordinate_x=current_coordinate_t[0]+delta_x
            new_coordinate_y=current_coordinate_t[1]+delta_y
            current_coordinate_t = (new_coordinate_x,new_coordinate_y)
            coordinates_x_l.append(new_coordinate_x)
            coordinates_y_l.append(new_coordinate_y)
        
        total_distance_x=current_coordinate_t[0]-origin_t[0]
        total_distance_y=current_coordinate_t[1]-origin_t[1]
        total_distance=((total_distance_x)**2+(total_distance_y)**2)**0.5

        distances_l.append(total_distance)
    
        if j in i_graph_l:
            plot = figure(title=(f"plot_{j}"))
            plot.line(coordinates_x_l,coordinates_y_l)
            show(plot)
            # export_png(plot, filename=(f"plot_{j}'.png"))
        
    distance_mean=statistics.mean(distances_l)
    distance_max=max(distances_l)
    distance_min=min(distances_l)

    return distance_mean, distance_max, distance_min

if __name__=="__main__":
    steps=10
    trials=10
    n_graphs=3
    d_m,d_max,d_min=drunkman_paths(steps,trials,n_graphs)
    print(f'random path of {steps} steps with {trials} trials')
    print(f'Mean = {d_m}')
    print(f'Max = {d_max}')
    print(f'Min = {d_min}')
