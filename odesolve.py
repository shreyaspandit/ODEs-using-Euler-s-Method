import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

class ODE(object):
    def __init__(self, initial_conditions, times, functions):
        self.states = initial_conditions
        self.initial_conditions = list(initial_conditions.values())
        self.times = times
        self.functions = functions
        self.number_of_equations = len(self.functions)
    
    def solve(self, step_size):
        """Initialize matrix with all zeros. The rows are for the timestamps and the columns of the value
        of each Y_k at that time."""
        values = np.zeros((int((self.times[1]-self.times[0])/step_size) + 1, self.number_of_equations + 1))
        values[0] = self.initial_conditions
        
        # Set timestamps
        for i in range(1, values.shape[0]):
            values[i][0] = times[0] + i*step_size
        
        # Apply Euler's Method
        for i in range(1, values.shape[0]):
            iterate = []
            for j in range(self.number_of_equations + 1):
                iterate.append(values[i-1][j])
            for k in range(1, self.number_of_equations + 1):
                values[i][k] = values[i-1][k] + step_size*self.functions[k-1](*iterate)
        
        return values
    
    
    
    def plot(self, output, multiple=False, phase=False):
        if multiple == True:
            fig, axs = plt.subplots(self.number_of_equations, 1, figsize=(10,10))
            for i in range(1, len(self.functions)+1):
                axs[i-1].scatter(output[:, 0], output[:, i], s = 1)
                axs[i-1].set_xlabel(list(self.states.keys())[0])
                axs[i-1].set_ylabel(list(self.states.keys())[i])
        elif multiple == False and phase == False:
            for i in range(1, len(self.functions)+1):
                #plt.scatter(output[:, 0], output[:, i], s = 1, label = list(self.states.keys())[i])
                plt.plot(output[:, 0], output[:, i], label=list(self.states.keys())[i], linewidth=1)
        else:
            if self.number_of_equations > 2:
                return "Error"
            else:
                dat = np.zeros((output.shape[0], 2))
                
                dat[:,0] = output[:,1]
                dat[:,1] = output[:,2]
                
                plt.xlabel(list(self.states.keys())[1])
                plt.ylabel(list(self.states.keys())[2])
                plt.plot(dat[:,0], dat[:,1])
            
        
        plt.legend(loc=2)    
        plt.show()
        
def dxdt(t, x):
    return x

functions = [dxdt]

initial_conditions = {"t": 0.00, "x": 1.00}
times = [-5.00, 10.00]

equations = ODE(initial_conditions, times, functions)
output = equations.solve(0.001)
equations.plot(output)
