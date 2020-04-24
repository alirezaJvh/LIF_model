import numpy as np
class LIF:
    def __init__(self, parameters):
        self.C = parameters['C']
        self.R = parameters['R']
        self.u_rest = parameters['u_rest']
        self.I = parameters['I']
        self.threshold = parameters['threshold']
        self.start_time = parameters['start_time']
        self.end_time = parameters['end_time']
        self.dt = parameters['dt']                    # step size (ms)

    def __tau_m(self):
        return self.C * self.R

    def time_length(self):
        return self.end_time - self.start_time

    def interval(self, I):
        array = np.empty(len(I))
        for i in range(len(I)):
            array[i] = self.__tau_m() * (np.log((self.R * I[i]) / (self.R * I[i] - self.threshold)))
        return array

    def __make_time_array_steps(self):
        return np.arange(0, self.end_time + self.dt, self.dt)

    def simulate(self, func=None):
        time = self.__make_time_array_steps()
        u_history = np.empty(len(time))
        self.I_history = np.empty(len(time))
        self.I_history[0] = 0
        u_history[0] = self.u_rest
        spike = 0
        for i in range(1, len(time)):
            if time[i] < self.start_time:
                u_history[i] = self.u_rest
                self.I_history[i] = 0
            else:
                if func is None:
                    # tau_m * (du/dt) = -(u - u_rest) + (R * I)
                    du = (1/self.__tau_m()) * (-(u_history[i-1] - self.u_rest) + (self.R * self.I))
                else:
                    # tau_m * (du/dt) = F(u) + (R * I)
                    du = (1/self.__tau_m()) * ((func(u_history[i-1], self.u_rest)) + (self.R * self.I))
                    print('here')

                u_history[i] = u_history[i - 1] + du * self.dt
                self.I_history[i] = self.I

            if u_history[i] > self.threshold:
                self.__reset_model(u_history, i)
                spike = spike + 1

        print(spike)
        return {"u": u_history, "time": time}

    def __reset_model(self, u, index):
        u[index] = self.u_rest
        u[index - 1] = self.threshold

    def get_I_history(self):
        return self.I_history