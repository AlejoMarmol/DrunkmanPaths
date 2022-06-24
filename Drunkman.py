import random
import matplotlib.pyplot as plt

class Drunkman:

    def __init__(self, name):
        self.name=name

class Drunkman_traditional(Drunkman):
    def __init__(self, name):
        super().__init__(name)
    
    def walk(self):
        return random.choice([(0, 1), (0, -1), (1, 0), (-1, 0)])

    def plot_path(self,x_l, y_l, origin_x, origin_y, final_x, final_y, trial_number, random_trial_number, n_trials, n_steps):
        plt.figure()
        plt.plot(x_l, y_l, 'k')
        plt.arrow(origin_x, origin_y, final_x, final_y , width=0.01 ,color='r')
        plt.title(f"Drunkman path for trial {random_trial_number} of {n_trials} with {n_steps} steps")
        plt.xlabel('x')
        plt.ylabel('y')
        plt.grid(True)
        plt.savefig(f"paths_plots/Drunkman path for trial {trial_number} of {n_trials} with {n_steps} steps.png")
