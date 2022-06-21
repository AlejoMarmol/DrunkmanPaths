import random
from turtle import color, width
from Drunkman import Drunkman_traditional
from Coordinate import Coordinate
from Field import Field
import statistics
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


# import numpy as np

def drunkman_paths(n_steps_l, n_trials, n_graphs,origin_t):

    drunkman_C=Drunkman_traditional(name='Rosalia')
    origin_C = Coordinate(origin_t[0],origin_t[1])
    field_C=Field(name='Madrid')

    distance_mean_l=[]
    distance_max_l=[]
    distance_min_l=[]



    # columns_l = 

    for n_steps in n_steps_l:

        distances_l=[]
        coordinates_l=[[],[]]
        i_graph_l=random.sample(range(0,n_trials),n_graphs) #remember to handle error
        i_graph_l.sort()
        print(i_graph_l)
        pp=1
        plt.figure()
        plt.suptitle(f"Drunkman path for {n_steps} steps")
        # p=0
        for p in range(n_trials):
            coordinates_x_l=[]
            coordinates_y_l=[]
            field_C.add_drunkman(drunkman_C,origin_C)
            coordinates_x_l.append(origin_C.x)
            coordinates_y_l.append(origin_C.y)
            
            for _ in range(n_steps):
                new_coordinate_C = field_C.move_drunkman(drunkman_C)
                coordinates_x_l.append(new_coordinate_C.x)
                coordinates_y_l.append(new_coordinate_C.y)
                current_coordinate_C=field_C.obtain_coordinates(drunkman_C)
            
            final_coordinate_C = current_coordinate_C
            total_distance = final_coordinate_C.distance(origin_C)

            distances_l.append(total_distance)

            
            if p in i_graph_l:
                # coordinates_l[0].append(coordinates_x_l)
                # coordinates_l[1].append(coordinates_y_l)
                
                plt.subplot(n_graphs,1,pp)
                plt.plot(coordinates_x_l,coordinates_y_l, 'k')
                plt.arrow(origin_C.x,origin_C.y,final_coordinate_C.x , final_coordinate_C.y , width=0.01 ,color='r')
                
                plt.xlabel('x')
                plt.ylabel('y')

                plt.grid(True)
                
                pp=pp+1
            
            
        plt.savefig(f"paths_plots/Drunkman path for trial {pp} of {n_trials} with {n_steps} steps.png")
        distance_mean=statistics.mean(distances_l)
        distance_max=max(distances_l)
        distance_min=min(distances_l)
        
        distance_mean_l.append(distance_mean)
        distance_max_l.append(distance_max)
        distance_min_l.append(distance_min)

        print(f'a random path from the drunkman {drunkman_C.name} of {n_steps} steps obtains:')
        print(f'Mean = {distance_mean}')
        print(f'Max = {distance_max}')
        print(f'Min = {distance_min}')
    
    drunkman_df = pd.DataFrame(columns=['Steps','Mean','Max','Min'])
    drunkman_df["Steps"] = n_steps_l
    drunkman_df["Mean"] = distance_mean_l
    drunkman_df["Max"] = distance_max_l
    drunkman_df["Min"] = distance_min_l
    drunkman_df.to_excel("drunkman_paths.xlsx")

      
    return distance_mean_l, distance_max_l, distance_min_l

if __name__=="__main__":
    n_steps_l=[10, 100, 1000, 10000]
    trials=10
    n_graphs=3
    d_m_l,d_max_l,d_min_l=drunkman_paths(n_steps_l,trials,n_graphs,origin_t=(0,0))
    # print(f'random path of {steps} steps with {trials} trials')
    # print(f'Mean = {d_m_l}')
    # print(f'Max = {d_max_l}')
    # print(f'Min = {d_min_l}')
