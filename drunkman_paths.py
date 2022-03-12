import random
import statistics
import matplotlib.pyplot as plt
import numpy as np

# import numpy as np

def drunkman_paths(n_steps_l, n_trials, n_graphs):

    distance_mean_l=[]
    distance_max_l=[]
    distance_min_l=[]

    for n_steps in n_steps_l:

        distances_l=[]
        coordinates_l=[[],[]]
        # i_graph_l=random.sample(range(0,n_trials),n_graphs) #remember to handle error
        # i_graph_l.sort()
        # print(i_graph_l)
        # p=0
        for _ in range(n_trials):
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

            
            # if j in i_graph_l:
            #     coordinates_l[0].append(coordinates_x_l)
            #     coordinates_l[1].append(coordinates_y_l)
            
            
        distance_mean=statistics.mean(distances_l)
        distance_max=max(distances_l)
        distance_min=min(distances_l)
        
        distance_mean_l.append(distance_mean)
        distance_max_l.append(distance_max)
        distance_min_l.append(distance_min)

    
    
    # plt.subplot(311)
    # plt.plot(coordinates_l[0][0],coordinates_l[1][0])
    # final_position_a=np.array([coordinates_l[0][0][-1]-origin_t[0],coordinates_l[1][0][-1]-origin_t[1]])
    # print(final_position_a)
    # # plt.quiver(final_position_a)
    # plt.plot([0,final_position_a[0]],[0,final_position_a[1]])
    # plt.xlabel(f'plot {i_graph_l[0]}')
    # plt.subplot(312)
    # plt.plot(coordinates_l[0][1],coordinates_l[1][1])
    # plt.xlabel(f'plot {i_graph_l[1]}')
    # plt.subplot(313)
    # plt.plot(coordinates_l[0][2],coordinates_l[1][2])
    # plt.xlabel(f'plot {i_graph_l[2]}')
    # plt.show()
    

    return distance_mean_l, distance_max_l, distance_min_l

if __name__=="__main__":
    n_steps_l=[10, 100, 1000, 10000]
    trials=10
    n_graphs=3
    d_m_l,d_max_l,d_min_l=drunkman_paths(n_steps_l,trials,n_graphs)
    # print(f'random path of {steps} steps with {trials} trials')
    print(f'Mean = {d_m_l}')
    print(f'Max = {d_max_l}')
    print(f'Min = {d_min_l}')
