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