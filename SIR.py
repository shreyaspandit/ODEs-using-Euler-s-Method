from odesolve import ODE

class SIR(ODE):
    def __init__(self, initial_conditions, times, parameters):
        self.states = initial_conditions
        self.initial_conditions = list(initial_conditions.values())
        self.times = times
        self.parameters = parameters
        self.number_of_equations = len(self.initial_conditions) - 1
    
    def model(self):
        def dS(t, S, I, R):
            N = S + I + R
            return -(self.parameters["beta"]*I*S)/N
        def dI(t, S, I, R):
            N = S + I + R
            return ((self.parameters["beta"]*I*S)/N) - self.parameters["gamma"]*I
        def dR(t, S, I, R):
            N = S + I + R
            return self.parameters["gamma"]*I
        
        self.functions = [dS, dI, dR]
        
  def SIR_Model(beta, gamma=0): 
    initial_conditions = {"t": 0.00, "S": 1000.00, "I": 1.00, "R": 0.00}
    times = [0, 100.00]
    parameters = {"beta": beta, "gamma": gamma}
    sir_model = SIR(initial_conditions, times, parameters)
    sir_model.model()
    output = sir_model.solve(0.01)
    sir_model.plot(output)
