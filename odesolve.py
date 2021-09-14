class ODE(object):
    def __init__(self, initial_conditions, times, functions):
        self.states = initial_conditions # initial_conditions is a dictionary eg. {"t": 0, "y_1": 1, "y_2": 2...}
        self.initial_conditions = list(initial_conditions.values()) # from above [0, 1, 2, ...]
        self.times = times # array with two elements: start time and end time
        self.functions = functions # name of function
        self.number_of_equations = len(self.functions) # the number of DEs to solve
    
    def solve(self, step_size):
        
        """
        
        Initialize matrix with all zeros. Each row is for a timestamp, and each column is for the value of Y_k at
        that timestamp. Ie. row i gives the values for each of t, Y_1, ... Y_n at time i.
        """
        
        values = np.zeros(( int((self.times[1]-self.times[0])/step_size) + 1, self.number_of_equations + 1 ))
        values[0] = self.initial_conditions # set first row as initial conditions
        
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
            plt.legend(loc=2) 
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
            
        
           
        plt.show()
