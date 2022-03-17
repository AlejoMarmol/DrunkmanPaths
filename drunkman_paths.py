import random
import statistics
import matplotlib.pyplot as plt
import numpy as np

# import numpy as np

class Drunkman:

    def __init__(self, name):
        self.name=name

class Drunkman_traditional(Drunkman):
    def __init__(self, name):
        super().__init__(name)
    
    def walk(self):
        return random.choice([(0, 1), (0, -1), (1, 0), (-1, 0)])

class Coordinate:

    def __init__(self,x,y):
        self.x=x
        self.y=y

    def move(self,delta_x,delta_y):
        return Coordinate(self.x + delta_x, self.y + delta_y)

    def distance(self, another_coordinate):
        delta_x=self.x - another_coordinate.x
        delta_y=self.y - another_coordinate.y

        return (delta_x**2 + delta_y**2)**0.5


def drunkman_paths(n_steps_l, n_trials, n_graphs,origin_t):

    drunkman_C=Drunkman_traditional(name='Rosalio')

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
            origin_C = Coordinate(origin_t[0],origin_t[1])
            current_coordinate_C=Coordinate(origin_C.x,origin_C.y)
            coordinates_x_l.append(origin_C.x)
            coordinates_y_l.append(origin_C.y)
            
            for _ in range(n_steps):
                delta_x, delta_y = drunkman_C.walk()
                new_coordinate_C = current_coordinate_C.move(delta_x,delta_y)
                coordinates_x_l.append(new_coordinate_C.x)
                coordinates_y_l.append(new_coordinate_C.y)
                current_coordinate_C.x = new_coordinate_C.x
                current_coordinate_C.y = new_coordinate_C.y
            
            final_coordinate_C = current_coordinate_C
            total_distance = final_coordinate_C.distance(origin_C)

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

        print(f'a random path from the drunkman {drunkman_C.name} of {n_steps} steps obtains:')
        print(f'Mean = {distance_mean}')
        print(f'Max = {distance_max}')
        print(f'Min = {distance_min}')

    
    
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
    d_m_l,d_max_l,d_min_l=drunkman_paths(n_steps_l,trials,n_graphs,origin_t=(0,0))
    # print(f'random path of {steps} steps with {trials} trials')
    # print(f'Mean = {d_m_l}')
    # print(f'Max = {d_max_l}')
    # print(f'Min = {d_min_l}')
