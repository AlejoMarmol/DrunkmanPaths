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

class Field:
    def __init__(self,name):
        self.drunkman_coordinates_d={}
        self.name=name
    
    def add_drunkman(self, drunkman_C, coordinate_C):
        self.drunkman_coordinates_d[drunkman_C] = coordinate_C
    
    def move_drunkman(self, drunkman_C):
        delta_x, delta_y = drunkman_C.walk()
        current_coordinate_C = self.drunkman_coordinates_d[drunkman_C]
        new_coordinate_C = current_coordinate_C.move(delta_x,delta_y)
        self.drunkman_coordinates_d[drunkman_C] = new_coordinate_C

        return new_coordinate_C
    
    def obtain_coordinates(self,drunkman_C):
        return self.drunkman_coordinates_d[drunkman_C]


def drunkman_paths(n_steps_l, n_trials, n_graphs,origin_t):

    drunkman_C=Drunkman_traditional(name='Rosalia')
    origin_C = Coordinate(origin_t[0],origin_t[1])
    field_C=Field(name='Madrid')

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
